import uuid
from typing import Optional, List, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, exc
from app.models.organization import (
    Organization,
    OrganizationMember,
    OrganizationRole,
    OrganizationStatus,
    OrganizationSettings,
    OrganizationSubscription,
    OrganizationAuditLog
)
from app.schemas.organization import OrganizationCreate, OrganizationUpdate
from fastapi import HTTPException
from app.services.workspace import workspace_service

class OrganizationService:
    async def create_organization(self, db: AsyncSession, org_in: OrganizationCreate, user_id: uuid.UUID) -> Organization:
        # Check if slug exists
        result = await db.execute(select(Organization).filter(Organization.slug == org_in.slug))
        if result.scalar_one_or_none():
            raise HTTPException(status_code=400, detail="Organization slug already exists")
            
        # Create Organization
        db_org = Organization(
            owner_id=user_id,
            created_by=user_id,
            name=org_in.name,
            slug=org_in.slug,
            description=org_in.description,
            logo_url=org_in.logo_url,
            industry=org_in.industry,
            company_size=org_in.company_size,
            country=org_in.country,
            timezone=org_in.timezone,
            status=OrganizationStatus.ACTIVE
        )
        db.add(db_org)
        await db.flush() # To get db_org.id
        
        # Create Owner Member
        member = OrganizationMember(
            organization_id=db_org.id,
            user_id=user_id,
            role=OrganizationRole.OWNER,
            status="ACTIVE"
        )
        db.add(member)
        
        # Create Settings
        settings = OrganizationSettings(
            organization_id=db_org.id,
            default_timezone=org_in.timezone or "UTC"
        )
        db.add(settings)
        
        # Create Subscription Reservation
        subscription = OrganizationSubscription(
            organization_id=db_org.id
        )
        db.add(subscription)
        
        # Create Audit Log
        audit_log = OrganizationAuditLog(
            organization_id=db_org.id,
            actor_id=user_id,
            event_type="organization.created",
            resource_type="organization",
            resource_id=str(db_org.id)
        )
        db.add(audit_log)
        
        await db.flush()
        
        # Create Canonical Workspace
        workspace = await workspace_service.create_workspace(
            db,
            name=db_org.name,
            slug=db_org.slug,
            user_id=user_id,
            organization_id=db_org.id,
            settings={}
        )
        
        # Provision AI Wallet for Organization
        from app.models.workspace import AIWallet
        wallet = AIWallet(
            workspace_id=workspace.id,
            balance_units=1000,
            monthly_grant=1000
        )
        db.add(wallet)
        
        await db.commit()
        await db.refresh(db_org)
        return db_org

    async def update_organization(
        self, db: AsyncSession, organization_id: uuid.UUID, org_in: "OrganizationUpdate", user_id: uuid.UUID
    ) -> Organization:
        stmt = select(Organization).where(Organization.id == organization_id)
        result = await db.execute(stmt)
        org = result.scalar_one_or_none()
        
        if not org:
            raise HTTPException(status_code=404, detail="Organization not found")
            
        update_data = org_in.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(org, field, value)
            
        # Create Audit Log
        audit_log = OrganizationAuditLog(
            organization_id=org.id,
            actor_id=user_id,
            action="ORGANIZATION_UPDATED",
            resource_type="organization",
            resource_id=str(org.id)
        )
        db.add(audit_log)
        
        await db.commit()
        await db.refresh(org)
        return org
        
    async def get_user_organizations(self, db: AsyncSession, user_id: uuid.UUID) -> List[Dict[str, Any]]:
        from sqlalchemy import func
        
        member_count_subq = (
            select(func.count(OrganizationMember.id))
            .where(OrganizationMember.organization_id == Organization.id)
            .where(OrganizationMember.status == "ACTIVE")
            .scalar_subquery()
            .correlate(Organization)
        )

        stmt = select(
            Organization,
            OrganizationMember.role.label("user_role"),
            member_count_subq.label("member_count")
        ).join(
            OrganizationMember, Organization.id == OrganizationMember.organization_id
        ).where(
            OrganizationMember.user_id == user_id,
            OrganizationMember.status == "ACTIVE"
        )
        
        result = await db.execute(stmt)
        
        orgs = []
        for org, role, member_count in result.all():
            orgs.append({
                "id": org.id,
                "slug": org.slug,
                "name": org.name,
                "logo_url": org.logo_url,
                "organization_status": org.status,
                "subscription_plan": None,  # Future expansion
                "user_role": role,
                "member_count": member_count,
                "created_at": org.created_at
            })
            
        # Sort organizations: Active active first then Alphabetically (if needed on backend)
        # However, the frontend usually does the active org sorting because active org is client state.
        # But we can pre-sort them alphabetically here for consistency.
        orgs.sort(key=lambda x: x["name"].lower())
            
        return orgs
        
    async def get_by_slug(self, db: AsyncSession, slug: str) -> Optional[Organization]:
        result = await db.execute(select(Organization).filter(Organization.slug == slug))
        return result.scalar_one_or_none()

    async def update_organization(
        self,
        db: AsyncSession,
        organization_id: uuid.UUID,
        org_in: OrganizationUpdate,
        actor_id: uuid.UUID
    ) -> Organization:
        org = await self.get_organization(db, organization_id)
        if not org:
            raise HTTPException(status_code=404, detail="Organization not found")
            
        update_data = org_in.model_dump(exclude_unset=True)
        if not update_data:
            return org
            
        old_values = {}
        new_values = {}
        for field, value in update_data.items():
            old_val = getattr(org, field, None)
            if old_val != value:
                old_values[field] = old_val
                new_values[field] = value
                setattr(org, field, value)
                
        if new_values:
            audit_log = OrganizationAuditLog(
                organization_id=organization_id,
                actor_id=actor_id,
                event_type="organization.updated",
                resource_type="organization",
                resource_id=str(org.id),
                old_values=old_values,
                new_values=new_values
            )
            db.add(audit_log)
            await db.commit()
            await db.refresh(org)
            
        return org

    async def get_organization(self, db: AsyncSession, organization_id: uuid.UUID) -> Optional[Organization]:
        return (await db.execute(select(Organization).where(Organization.id == organization_id))).scalar_one_or_none()

    async def get_organization_stats(self, db: AsyncSession, organization_id: uuid.UUID) -> dict:
        from app.models.project import Project, Repository
        from app.models.team import Team
        from app.models.bug import Bug
        from sqlalchemy import func
        
        projects_count = (await db.execute(select(func.count(Project.id)).where(Project.organization_id == organization_id))).scalar() or 0
        repositories_count = (await db.execute(select(func.count(Repository.id)).where(Repository.organization_id == organization_id))).scalar() or 0
        members_count = (await db.execute(select(func.count(OrganizationMember.id)).where(OrganizationMember.organization_id == organization_id, OrganizationMember.status == "ACTIVE"))).scalar() or 0
        teams_count = (await db.execute(select(func.count(Team.id)).where(Team.organization_id == organization_id))).scalar() or 0
        open_bugs_count = (await db.execute(select(func.count(Bug.id)).join(Project, Bug.project_id == Project.id).where(Project.organization_id == organization_id, Bug.state.in_(["OPEN", "ANALYZING", "RECOMMENDATION_READY", "ASSIGNED"])))).scalar() or 0
        closed_bugs_count = (await db.execute(select(func.count(Bug.id)).join(Project, Bug.project_id == Project.id).where(Project.organization_id == organization_id, Bug.state.in_(["RESOLVED", "CLOSED"])))).scalar() or 0
        indexed_repositories_count = (await db.execute(select(func.count(Repository.id)).where(Repository.organization_id == organization_id, Repository.sync_status == "COMPLETED"))).scalar() or 0
        
        sub = (await db.execute(select(OrganizationSubscription).where(OrganizationSubscription.organization_id == organization_id))).scalar_one_or_none()
        seat_limit = sub.seat_limit if sub else 5
        
        return {
            "projects_count": projects_count,
            "repositories_count": repositories_count,
            "members_count": members_count,
            "teams_count": teams_count,
            "open_bugs_count": open_bugs_count,
            "closed_bugs_count": closed_bugs_count,
            "indexed_repositories_count": indexed_repositories_count,
            "ai_usage_count": 0, # Placeholder until AI usage model is added
            "storage_used_bytes": 0, # Placeholder
            "seat_usage": members_count,
            "seat_limit": seat_limit
        }

    async def get_member_public_profile(
        self, db: AsyncSession, organization_id: uuid.UUID, user_id: uuid.UUID
    ) -> Optional[dict]:
        from app.models.identity import User
        from app.models.developer import DeveloperProfile
        from app.models.project import Project, Repository
        from app.models.bug import Bug
        from sqlalchemy import func, select
        
        # 1. Validate Membership
        member_stmt = select(OrganizationMember).where(
            OrganizationMember.organization_id == organization_id,
            OrganizationMember.user_id == user_id,
            OrganizationMember.status == "ACTIVE"
        )
        member = (await db.execute(member_stmt)).scalar_one_or_none()
        if not member:
            return None
            
        # 2. Get User and Profile
        user = (await db.execute(select(User).where(User.id == user_id))).scalar_one_or_none()
        profile = (await db.execute(select(DeveloperProfile).where(DeveloperProfile.user_id == user_id))).scalar_one_or_none()
        
        if not user:
            return None
            
        # 3. Aggregate Stats
        # These can be optimized as needed, for now we run distinct lightweight counts
        assigned_bugs = 0 # Placeholder until we have bug assignments modeled properly (e.g. BugAssignee)
        resolved_bugs = 0 # Placeholder
        
        # 4. Construct Public Profile
        # Follow the PublicProfileResponse schema
        public_profile = {
            "user_id": user.id,
            "full_name": user.full_name or "Unknown User",
            "avatar_url": getattr(user, 'avatar_url', None) or (profile.github_avatar_url if profile else None),
            "organization_role": member.role.value,
            "developer_title": profile.designation if profile else "Developer",
            "bio": profile.bio if profile else None,
            "location": profile.location if profile else None,
            "timezone": profile.timezone if profile else None,
            "skills": profile.skills if profile else None,
            "github_username": profile.github_username if profile else None,
            "repositories_connected": profile.github_public_repos if profile and profile.github_public_repos else 0,
            "projects_participated": 0, # Future placeholder
            "assigned_bugs": assigned_bugs,
            "resolved_bugs": resolved_bugs,
            "developer_score": 0, # AI Placeholder
            "joined_at": member.created_at.isoformat() if getattr(member, 'created_at', None) else None,
            "last_active": user.updated_at.isoformat() if getattr(user, 'updated_at', None) else None,
            "availability_status": profile.availability if profile else "Available",
        }
        
        return public_profile

organization_service = OrganizationService()
