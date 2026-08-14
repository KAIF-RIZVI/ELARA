import uuid
from typing import Optional, List, Dict, Any
from datetime import datetime, timedelta, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, desc, or_
from app.models.organization import Organization, OrganizationMember, OrganizationAuditLog, OrganizationSubscription, OrganizationInvitation
from app.models.project import Project, Repository
from app.models.bug import Bug, BugState
from app.models.ai import Recommendation
from app.models.identity import User
from app.models.developer import DeveloperProfile
from app.schemas.dashboard import DashboardActivityType

def _calculate_health_score(stats: dict) -> tuple[int, str]:
    score = 100
    
    # Deduct for critical open bugs
    if stats.get('bugs_critical', 0) > 0:
        score -= min(30, stats['bugs_critical'] * 10)
        
    # Deduct for having projects but no repos
    if stats.get('projects_total', 0) > 0 and stats.get('repositories_total', 0) == 0:
        score -= 10
        
    score = max(0, score)
    
    status = "Healthy"
    if score < 70:
        status = "Critical"
    elif score < 90:
        status = "Needs Attention"
        
    return score, status

class OrganizationDashboardService:
    async def get_dashboard_data(self, db: AsyncSession, organization_id: uuid.UUID, user_id: uuid.UUID) -> dict:
        # Get organization and user role
        org_result = await db.execute(select(Organization).where(Organization.id == organization_id))
        org = org_result.scalar_one_or_none()
        if not org:
            return None

        member_result = await db.execute(
            select(OrganizationMember)
            .where(OrganizationMember.organization_id == organization_id, OrganizationMember.user_id == user_id)
        )
        member = member_result.scalar_one_or_none()
        if not member:
            return None
            
        # Get owner name
        owner_result = await db.execute(
            select(User.full_name)
            .join(OrganizationMember, User.id == OrganizationMember.user_id)
            .where(OrganizationMember.organization_id == organization_id, OrganizationMember.role == "OWNER")
            .limit(1)
        )
        owner_name = owner_result.scalar_one_or_none() or "Owner"
        
        # Pending invitations
        pending_invites = await db.scalar(
            select(func.count(OrganizationInvitation.id))
            .where(OrganizationInvitation.organization_id == organization_id, OrganizationInvitation.status == "PENDING")
        )

        seven_days_ago = datetime.now(timezone.utc) - timedelta(days=7)
        seven_days_ago_naive = seven_days_ago.replace(tzinfo=None)

        # 1. Statistics Aggregation
        members_total = await db.scalar(select(func.count(OrganizationMember.id)).where(OrganizationMember.organization_id == organization_id, OrganizationMember.status == "ACTIVE")) or 0
        members_active = await db.scalar(select(func.count(OrganizationMember.id)).where(OrganizationMember.organization_id == organization_id, OrganizationMember.status == "ACTIVE", OrganizationMember.created_at >= seven_days_ago_naive)) or 0
        
        projects_total = await db.scalar(select(func.count(Project.id)).where(Project.organization_id == organization_id)) or 0
        projects_active = await db.scalar(select(func.count(Project.id)).where(Project.organization_id == organization_id, Project.updated_at >= seven_days_ago_naive)) or 0
        
        repos_total = await db.scalar(select(func.count(Repository.id)).where(Repository.organization_id == organization_id)) or 0
        
        # Get org project IDs
        proj_ids_result = await db.execute(select(Project.id).where(Project.organization_id == organization_id))
        project_ids = [row[0] for row in proj_ids_result.fetchall()]
        
        bugs_open = 0
        bugs_critical = 0
        ai_jobs_total = 0
        
        if project_ids:
            # Bug counts
            bugs_open = await db.scalar(
                select(func.count(Bug.id))
                .where(Bug.project_id.in_(project_ids), Bug.state != BugState.CLOSED)
            ) or 0
            
            bugs_critical = await db.scalar(
                select(func.count(Bug.id))
                .where(Bug.project_id.in_(project_ids), Bug.state != BugState.CLOSED, Bug.severity == "CRITICAL")
            ) or 0

        # Repositories indexed (ai_ready)
        repos_indexed = await db.scalar(
            select(func.count(Repository.id))
            .where(Repository.organization_id == organization_id, Repository.sync_status == "COMPLETED")
        ) or 0

        # (Removed heavy queries for recent projects, repos, bugs, and members)

        # 6. Recent Activity
        activity_result = await db.execute(
            select(OrganizationAuditLog, User.full_name, User.avatar_url)
            .outerjoin(User, OrganizationAuditLog.actor_id == User.id)
            .where(OrganizationAuditLog.organization_id == organization_id)
            .order_by(desc(OrganizationAuditLog.created_at))
            .limit(10)
        )
        recent_activity = []
        last_activity_at = org.updated_at.isoformat() if org.updated_at else None
        
        for a, u_name, u_avatar in activity_result.all():
            if not last_activity_at:
                last_activity_at = a.created_at.isoformat() if getattr(a, 'created_at', None) else None
                
            # Map audit log event_type to new DashboardActivityType
            event_type = DashboardActivityType.member_joined # default fallback
            title = "Activity"
            desc_text = ""
            
            if a.event_type == "organization.updated":
                title = "Organization Updated"
                desc_text = "Organization settings were updated."
                event_type = DashboardActivityType.project_created # fallback since org updated isnt an enum
            elif a.event_type == "member.invited":
                title = "Member Invited"
                desc_text = "A new invitation was sent."
                event_type = DashboardActivityType.invitation_created
            elif a.event_type == "member.joined":
                title = "Member Joined"
                desc_text = "A new member joined the organization."
                event_type = DashboardActivityType.member_joined
            elif a.event_type == "project.created":
                title = "Project Created"
                desc_text = "A new project was created."
                event_type = DashboardActivityType.project_created
            elif a.event_type == "repository.connected":
                title = "Repository Connected"
                desc_text = "A repository was successfully connected."
                event_type = DashboardActivityType.repository_connected
            elif a.event_type == "bug.created":
                title = "Bug Reported"
                desc_text = "A new bug was reported."
                event_type = DashboardActivityType.bug_created
            elif a.event_type == "bug.resolved":
                title = "Bug Resolved"
                desc_text = "A bug was marked as resolved."
                event_type = DashboardActivityType.bug_closed
            
            recent_activity.append({
                "id": a.id,
                "type": event_type,
                "actor": u_name or "System",
                "actor_avatar": u_avatar,
                "title": title,
                "description": desc_text,
                "created_at": a.created_at.isoformat() if getattr(a, 'created_at', None) else ""
            })

        return {
            "id": org.id,
            "name": org.name,
            "slug": org.slug,
            "avatar": getattr(org, 'logo_url', None),
            "description": org.description,
            "created_at": org.created_at.isoformat() if org.created_at else "",
            "updated_at": org.updated_at.isoformat() if org.updated_at else "",
            "last_activity_at": org.updated_at.isoformat() if org.updated_at else "", # Mocked using updated_at for now
            "owner": owner_name,
            "member_count": members_total,
            "project_count": projects_total,
            "repository_count": repos_total,
            "pending_invitation_count": pending_invites,
            "active_status": "Active" if getattr(org, 'status', None) == "ACTIVE" else "Inactive",
            
            "statistics": {
                "members_total": members_total,
                "members_active": members_active,
                "projects_total": projects_total,
                "projects_active": projects_active,
                "repositories_total": repos_total,
                "repositories_indexed": repos_indexed,
                "bugs_open": bugs_open,
                "bugs_critical": bugs_critical
            },
            
            "recent_activity": recent_activity
        }

organization_dashboard_service = OrganizationDashboardService()
