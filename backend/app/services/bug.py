import uuid
import datetime
from typing import Sequence, Any, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, desc

from app.core.base_service import BaseService
from app.models.bug import Bug, BugState, BugPriority, BugAssignment, BugComment, BugSource
from app.schemas.bug import BugCreate, BugUpdate, BugStatusUpdate, BugPriorityUpdate, BugAssignUpdate, BugCommentCreate
from app.models.workspace import Workspace, ActivityLog
from app.models.identity import WorkspaceMember
from app.models.organization import OrganizationMember

VALID_TRANSITIONS = {
    BugState.OPEN: {BugState.TRIAGED, BugState.IN_PROGRESS, BugState.CLOSED, BugState.DUPLICATE, BugState.WONT_FIX},
    BugState.TRIAGED: {BugState.IN_PROGRESS, BugState.CLOSED, BugState.DUPLICATE, BugState.WONT_FIX},
    BugState.IN_PROGRESS: {BugState.RESOLVED, BugState.BLOCKED, BugState.CLOSED},
    BugState.BLOCKED: {BugState.IN_PROGRESS, BugState.CLOSED},
    BugState.RESOLVED: {BugState.VERIFIED, BugState.CLOSED, BugState.REOPENED},
    BugState.VERIFIED: {BugState.CLOSED, BugState.REOPENED},
    BugState.CLOSED: {BugState.REOPENED},
    BugState.REOPENED: {BugState.IN_PROGRESS, BugState.TRIAGED, BugState.CLOSED, BugState.RESOLVED},
    BugState.DUPLICATE: {BugState.REOPENED},
    BugState.WONT_FIX: {BugState.REOPENED},
}

class BugService:
    async def create_bug(
        self, db: AsyncSession, *, obj_in: BugCreate, organization_id: uuid.UUID, workspace_id: uuid.UUID, user_id: Optional[uuid.UUID] = None, source: BugSource = BugSource.MANUAL, commit: bool = True
    ) -> Bug:
        # Check legacy workspace safety and tenant isolation
        workspace = await db.scalar(select(Workspace).where(Workspace.id == workspace_id))
        if not workspace:
            raise ValueError("Workspace not found.")
        if workspace.organization_id is None:
            raise ValueError("Legacy workspaces without an organization cannot create bugs. Please migrate the workspace.")
        if workspace.organization_id != organization_id:
            raise ValueError("Workspace does not belong to the authorized organization.")

        async with db.begin_nested():
            db_obj = Bug(
                organization_id=organization_id,
                workspace_id=workspace_id,
                title=obj_in.title,
                description=obj_in.description,
                priority=obj_in.priority,
                severity=obj_in.severity,
                project_id=obj_in.project_id,
                repository_id=obj_in.repository_id,
                environment=obj_in.environment,
                reproduction_steps=obj_in.reproduction_steps,
                expected_behavior=obj_in.expected_behavior,
                actual_behavior=obj_in.actual_behavior,
                reporter_metadata=obj_in.reporter_metadata,
                category=obj_in.category,
                external_ref=obj_in.external_ref,
                stack_trace=obj_in.stack_trace,
                state=BugState.OPEN,
                reported_by=user_id,
                source=source
            )
            db.add(db_obj)
            await db.flush()

            activity = ActivityLog(
                workspace_id=workspace_id,
                organization_id=organization_id,
                bug_id=db_obj.id,
                action="BUG_CREATED",
                target=db_obj.title,
                status="success",
                user_id=user_id,
                metadata_payload={"priority": db_obj.priority.value, "severity": db_obj.severity.value, "state": db_obj.state.value}
            )
            db.add(activity)

        if commit:
            await db.commit()
            await db.refresh(db_obj)
        return db_obj

    async def get_bug(self, db: AsyncSession, bug_id: uuid.UUID, organization_id: uuid.UUID, workspace_id: uuid.UUID) -> Optional[Bug]:
        stmt = select(Bug).where(
            Bug.id == bug_id,
            Bug.organization_id == organization_id,
            Bug.workspace_id == workspace_id,
            Bug.is_deleted == False
        )
        return await db.scalar(stmt)

    async def list_bugs(self, db: AsyncSession, organization_id: uuid.UUID, workspace_id: uuid.UUID) -> Sequence[Bug]:
        stmt = select(Bug).where(
            Bug.organization_id == organization_id,
            Bug.workspace_id == workspace_id,
            Bug.is_deleted == False
        ).order_by(Bug.created_at.desc())
        result = await db.execute(stmt)
        return result.scalars().all()

    async def list_organization_bugs(self, db: AsyncSession, organization_id: uuid.UUID) -> Sequence[Bug]:
        stmt = select(Bug).where(
            Bug.organization_id == organization_id,
            Bug.is_deleted == False
        ).order_by(Bug.created_at.desc())
        result = await db.execute(stmt)
        return result.scalars().all()

    async def update_bug(
        self, db: AsyncSession, *, bug_id: uuid.UUID, obj_in: BugUpdate, organization_id: uuid.UUID, workspace_id: uuid.UUID, user_id: uuid.UUID
    ) -> Bug:
        bug = await self.get_bug(db, bug_id, organization_id, workspace_id)
        if not bug:
            raise ValueError("Bug not found or unauthorized.")

        update_data = obj_in.model_dump(exclude_unset=True)
        if not update_data:
            return bug

        async with db.begin_nested():
            for field, value in update_data.items():
                setattr(bug, field, value)
            
            activity = ActivityLog(
                workspace_id=workspace_id,
                organization_id=organization_id,
                bug_id=bug.id,
                action="BUG_UPDATED",
                target=bug.title,
                status="success",
                user_id=user_id,
                metadata_payload={"updated_fields": list(update_data.keys())}
            )
            db.add(activity)

        await db.commit()
        await db.refresh(bug)
        return bug

    async def change_status(
        self, db: AsyncSession, *, bug_id: uuid.UUID, obj_in: BugStatusUpdate, organization_id: uuid.UUID, workspace_id: uuid.UUID, user_id: uuid.UUID
    ) -> Bug:
        bug = await self.get_bug(db, bug_id, organization_id, workspace_id)
        if not bug:
            raise ValueError("Bug not found or unauthorized.")

        if bug.state == obj_in.state:
            return bug

        if obj_in.state not in VALID_TRANSITIONS.get(bug.state, set()):
            raise ValueError(f"Invalid state transition from {bug.state.value} to {obj_in.state.value}")

        async with db.begin_nested():
            old_state = bug.state
            bug.state = obj_in.state

            if obj_in.state == BugState.CLOSED and old_state != BugState.CLOSED:
                bug.closed_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
            if obj_in.state == BugState.RESOLVED and old_state != BugState.RESOLVED:
                bug.resolved_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
            if obj_in.state == BugState.REOPENED:
                bug.closed_at = None
                bug.resolved_at = None

            activity_action = "STATUS_CHANGED"
            if obj_in.state == BugState.CLOSED:
                activity_action = "BUG_CLOSED"
            elif obj_in.state == BugState.RESOLVED:
                activity_action = "BUG_RESOLVED"
            elif obj_in.state == BugState.REOPENED:
                activity_action = "BUG_REOPENED"

            activity = ActivityLog(
                workspace_id=workspace_id,
                organization_id=organization_id,
                bug_id=bug.id,
                action=activity_action,
                target=f"{bug.title} ({old_state.value} -> {bug.state.value})",
                status="success",
                user_id=user_id,
                metadata_payload={"old_state": old_state.value, "new_state": bug.state.value}
            )
            db.add(activity)

        await db.commit()
        await db.refresh(bug)
        return bug

    async def change_priority(
        self, db: AsyncSession, *, bug_id: uuid.UUID, obj_in: BugPriorityUpdate, organization_id: uuid.UUID, workspace_id: uuid.UUID, user_id: uuid.UUID
    ) -> Bug:
        bug = await self.get_bug(db, bug_id, organization_id, workspace_id)
        if not bug:
            raise ValueError("Bug not found or unauthorized.")

        if bug.priority == obj_in.priority:
            return bug

        async with db.begin_nested():
            old_priority = bug.priority
            bug.priority = obj_in.priority

            activity = ActivityLog(
                workspace_id=workspace_id,
                organization_id=organization_id,
                bug_id=bug.id,
                action="PRIORITY_CHANGED",
                target=f"{bug.title} ({old_priority.value} -> {bug.priority.value})",
                status="success",
                user_id=user_id,
                metadata_payload={"old_priority": old_priority.value, "new_priority": bug.priority.value}
            )
            db.add(activity)

        await db.commit()
        await db.refresh(bug)
        return bug

    async def assign_developer(
        self, db: AsyncSession, *, bug_id: uuid.UUID, obj_in: BugAssignUpdate, organization_id: uuid.UUID, workspace_id: uuid.UUID, user_id: uuid.UUID
    ) -> Bug:
        bug = await self.get_bug(db, bug_id, organization_id, workspace_id)
        if not bug:
            raise ValueError("Bug not found or unauthorized.")

        developer_id = obj_in.developer_id

        async with db.begin_nested():
            # Soft-remove current active assignments
            stmt = select(BugAssignment).where(
                BugAssignment.bug_id == bug_id,
                BugAssignment.removed_at.is_(None)
            )
            current_assignments = (await db.execute(stmt)).scalars().all()
            for assignment in current_assignments:
                assignment.removed_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
            
            if developer_id is not None:
                # Verify developer belongs to workspace
                stmt_member = select(WorkspaceMember).where(
                    WorkspaceMember.workspace_id == workspace_id,
                    WorkspaceMember.user_id == developer_id
                )
                member = await db.scalar(stmt_member)
                if not member:
                    raise ValueError("Assignee is not a valid member of this workspace.")

                new_assignment = BugAssignment(
                    bug_id=bug_id,
                    workspace_id=workspace_id,
                    organization_id=organization_id,
                    developer_id=developer_id,
                    assigned_by=user_id,
                    assigned_at=datetime.datetime.now(datetime.timezone.utc).isoformat()
                )
                db.add(new_assignment)
                
                activity = ActivityLog(
                    workspace_id=workspace_id,
                    organization_id=organization_id,
                    bug_id=bug.id,
                    action="BUG_ASSIGNED",
                    target=bug.title,
                    status="success",
                    user_id=user_id,
                    metadata_payload={"developer_id": str(developer_id)}
                )
            else:
                activity = ActivityLog(
                    workspace_id=workspace_id,
                    organization_id=organization_id,
                    bug_id=bug.id,
                    action="BUG_UNASSIGNED",
                    target=bug.title,
                    status="success",
                    user_id=user_id
                )
                
            db.add(activity)

        await db.commit()
        await db.refresh(bug)
        return bug

    async def add_comment(
        self, db: AsyncSession, *, bug_id: uuid.UUID, obj_in: BugCommentCreate, organization_id: uuid.UUID, workspace_id: uuid.UUID, user_id: uuid.UUID
    ) -> BugComment:
        bug = await self.get_bug(db, bug_id, organization_id, workspace_id)
        if not bug:
            raise ValueError("Bug not found or unauthorized.")

        async with db.begin_nested():
            comment = BugComment(
                bug_id=bug_id,
                organization_id=organization_id,
                workspace_id=workspace_id,
                author_id=user_id,
                body=obj_in.body
            )
            db.add(comment)

            await db.flush()

            activity = ActivityLog(
                workspace_id=workspace_id,
                organization_id=organization_id,
                bug_id=bug.id,
                action="BUG_COMMENTED",
                target=bug.title,
                status="success",
                user_id=user_id,
                metadata_payload={"comment_id": str(comment.id)}
            )
            db.add(activity)
            
        await db.commit()
        await db.refresh(comment)
        return comment

    async def list_comments(
        self, db: AsyncSession, *, bug_id: uuid.UUID, organization_id: uuid.UUID, workspace_id: uuid.UUID
    ) -> Sequence[BugComment]:
        # ensure bug exists & is authorized
        bug = await self.get_bug(db, bug_id, organization_id, workspace_id)
        if not bug:
            raise ValueError("Bug not found or unauthorized.")

        stmt = select(BugComment).where(
            BugComment.bug_id == bug_id,
            BugComment.is_deleted == False
        ).order_by(BugComment.created_at.asc())
        result = await db.execute(stmt)
        return result.scalars().all()

    async def delete_bug(
        self, db: AsyncSession, *, bug_id: uuid.UUID, organization_id: uuid.UUID, workspace_id: uuid.UUID, user_id: uuid.UUID
    ) -> None:
        bug = await self.get_bug(db, bug_id, organization_id, workspace_id)
        if not bug:
            raise ValueError("Bug not found or unauthorized.")

        async with db.begin_nested():
            bug.is_deleted = True
            bug.deleted_at = datetime.datetime.now(datetime.timezone.utc)
            
            activity = ActivityLog(
                workspace_id=workspace_id,
                organization_id=organization_id,
                bug_id=bug.id,
                action="BUG_DELETED",
                target=bug.title,
                status="success",
                user_id=user_id
            )
            db.add(activity)
            
        await db.commit()

    async def get_bug_history(
        self, db: AsyncSession, *, bug_id: uuid.UUID, organization_id: uuid.UUID, workspace_id: uuid.UUID
    ) -> Sequence[ActivityLog]:
        bug = await self.get_bug(db, bug_id, organization_id, workspace_id)
        if not bug:
            raise ValueError("Bug not found or unauthorized.")

        stmt = select(ActivityLog).where(
            ActivityLog.bug_id == bug_id,
            ActivityLog.organization_id == organization_id,
            ActivityLog.workspace_id == workspace_id
        ).order_by(ActivityLog.created_at.desc())
        result = await db.execute(stmt)
        return result.scalars().all()

bug_service = BugService()
