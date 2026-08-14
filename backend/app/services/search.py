import time
import uuid
from typing import Optional, List, Dict
from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.identity import User
from app.models.organization import Organization, OrganizationMember
from app.models.project import Project, Repository
from app.models.bug import Bug
from app.models.team import Team

from app.schemas.search import (
    SearchCategory,
    SearchResultItem,
    GlobalSearchResponse
)

class GlobalSearchService:
    @staticmethod
    async def search(
        db: AsyncSession,
        current_user: User,
        query: str,
        organization_id: Optional[uuid.UUID] = None,
        category_filter: Optional[str] = None,
        limit: int = 10
    ) -> GlobalSearchResponse:
        start_time = time.time()
        
        # Parse query for prefixes
        q = query.strip()
        prefix_filter = None
        
        if ":" in q:
            parts = q.split(":", 1)
            possible_prefix = parts[0].lower()
            if possible_prefix in ["repo", "project", "bug", "member", "team", "org", "setting"]:
                prefix_filter = possible_prefix
                q = parts[1].strip()

        # If there's an explicit category filter from API, override prefix
        if category_filter:
            prefix_filter = category_filter.lower()

        search_pattern = f"%{q}%" if q else None
        
        # Base RBAC: get all org IDs the user belongs to
        stmt = select(OrganizationMember.organization_id).filter(OrganizationMember.user_id == current_user.id)
        result = await db.execute(stmt)
        user_org_ids = [row[0] for row in result.all()]

        if organization_id and organization_id in user_org_ids:
            allowed_org_ids = [organization_id]
        else:
            allowed_org_ids = user_org_ids

        results = SearchCategory()

        if not allowed_org_ids and not q:
            return GlobalSearchResponse(
                results=results,
                query=query,
                took_ms=int((time.time() - start_time) * 1000)
            )

        # 1. Organizations
        if not prefix_filter or prefix_filter == "org":
            org_stmt = select(Organization).filter(Organization.id.in_(allowed_org_ids))
            if search_pattern:
                org_stmt = org_stmt.filter(
                    or_(
                        Organization.name.ilike(search_pattern),
                        Organization.slug.ilike(search_pattern)
                    )
                )
            org_stmt = org_stmt.limit(limit)
            org_result = await db.execute(org_stmt)
            orgs = org_result.scalars().all()
            for o in orgs:
                results.organizations.append(
                    SearchResultItem(
                        id=str(o.id),
                        title=o.name,
                        subtitle="Organization",
                        category="organizations",
                        url=f"/organizations/{o.slug}",
                        organization_id=o.id
                    )
                )

        # 2. Projects
        if not prefix_filter or prefix_filter == "project":
            proj_stmt = select(Project, Organization.slug.label("org_slug")).join(
                Organization, Project.organization_id == Organization.id
            ).filter(Project.organization_id.in_(allowed_org_ids))
            if search_pattern:
                proj_stmt = proj_stmt.filter(Project.name.ilike(search_pattern))
            proj_stmt = proj_stmt.limit(limit)
            proj_result = await db.execute(proj_stmt)
            for p, org_slug in proj_result.all():
                results.projects.append(
                    SearchResultItem(
                        id=str(p.id),
                        title=p.name,
                        subtitle="Project",
                        category="projects",
                        url=f"/organizations/{org_slug}/projects/{p.id}",
                        organization_id=p.organization_id
                    )
                )

        # 3. Repositories
        if not prefix_filter or prefix_filter == "repo":
            repo_stmt = select(Repository).join(Project).options(selectinload(Repository.project).selectinload(Project.organization)).filter(Project.organization_id.in_(allowed_org_ids))
            if search_pattern:
                repo_stmt = repo_stmt.filter(Repository.name.ilike(search_pattern))
            repo_stmt = repo_stmt.limit(limit)
            repo_result = await db.execute(repo_stmt)
            repos = repo_result.scalars().all()
            for r in repos:
                results.repositories.append(
                    SearchResultItem(
                        id=str(r.id),
                        title=r.name,
                        subtitle=r.project.name if r.project else "Repository",
                        category="repositories",
                        url=f"/organizations/{r.project.organization.slug}/projects/{r.project_id}/repositories/{r.id}" if r.project else "#",
                        organization_id=r.project.organization_id if r.project else None
                    )
                )

        # 4. Bugs
        if not prefix_filter or prefix_filter == "bug":
            bug_stmt = select(Bug).join(Project).options(selectinload(Bug.project).selectinload(Project.organization)).filter(Project.organization_id.in_(allowed_org_ids))
            if search_pattern:
                bug_stmt = bug_stmt.filter(
                    or_(
                        Bug.title.ilike(search_pattern),
                        Bug.human_id.ilike(search_pattern)
                    )
                )
            bug_stmt = bug_stmt.limit(limit)
            bug_result = await db.execute(bug_stmt)
            bugs = bug_result.scalars().all()
            for b in bugs:
                results.bugs.append(
                    SearchResultItem(
                        id=str(b.id),
                        title=b.title,
                        subtitle=b.human_id,
                        category="bugs",
                        url=f"/organizations/{b.project.organization.slug}/projects/{b.project_id}/bugs/{b.id}" if b.project else "#",
                        organization_id=b.project.organization_id if b.project else None
                    )
                )

        # 5. Members
        if not prefix_filter or prefix_filter == "member":
            member_stmt = select(User).join(OrganizationMember).filter(OrganizationMember.organization_id.in_(allowed_org_ids))
            if search_pattern:
                member_stmt = member_stmt.filter(
                    or_(
                        User.first_name.ilike(search_pattern),
                        User.last_name.ilike(search_pattern),
                        User.email.ilike(search_pattern)
                    )
                )
            member_stmt = member_stmt.limit(limit)
            member_result = await db.execute(member_stmt)
            members = member_result.scalars().unique().all()
            for m in members:
                results.members.append(
                    SearchResultItem(
                        id=str(m.id),
                        title=f"{m.first_name or ''} {m.last_name or ''}".strip() or m.email,
                        subtitle=m.email,
                        category="members",
                        url=f"/profile/{m.id}",
                        organization_id=None
                    )
                )

        took_ms = int((time.time() - start_time) * 1000)
        return GlobalSearchResponse(
            results=results,
            query=query,
            took_ms=took_ms
        )
