import asyncio
import logging
import uuid
from datetime import datetime, timezone, timedelta
from app.worker.celery_app import celery_app
from app.core.database import AsyncSessionLocal as SessionLocal
from app.models.organization import Organization, OrganizationStatus
from app.models.project import RepoIndexJob, JobStatus
from app.ai.vector_store import vector_store
from app.models.notification import Notification, NotificationType, NotificationPriority
from app.models.organization import OrganizationMember
from sqlalchemy import select, update

logger = logging.getLogger(__name__)

def _run_async(coro):
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    return loop.run_until_complete(coro)

@celery_app.task(name="delete_organization_task", bind=True, max_retries=3)
def delete_organization_task(self, organization_id_str: str):
    """
    Safely deletes an organization with strict quiescence checks.
    """
    organization_id = uuid.UUID(organization_id_str)
    
    async def _execute():
        async with SessionLocal() as db:
            # Step 1: Pre-flight lock
            org = await db.scalar(select(Organization).where(Organization.id == organization_id))
            if not org:
                logger.info(f"Organization {organization_id} not found. Already deleted.")
                return {"status": "ALREADY_DELETED"}

            if org.status != OrganizationStatus.DELETING:
                org.status = OrganizationStatus.DELETING
                await db.commit()
                logger.info(f"Marked Organization {organization_id} as DELETING.")

            # Step 2: Cancel queued/active jobs
            active_statuses = [
                JobStatus.QUEUED, JobStatus.CLONING, JobStatus.PARSING,
                JobStatus.ANALYZING, JobStatus.EMBEDDING, JobStatus.STORING
            ]
            
            stmt = update(RepoIndexJob).where(
                RepoIndexJob.organization_id == organization_id,
                RepoIndexJob.status.in_(active_statuses)
            ).values(
                status=JobStatus.CANCELLED,
                error="Cancelled due to organization deletion."
            )
            await db.execute(stmt)
            await db.commit()

            # Step 3: Quiescence Mechanism
            timeout = 300  # 5 minutes
            start_time = datetime.now(timezone.utc)
            quiescent = False
            
            while (datetime.now(timezone.utc) - start_time).total_seconds() < timeout:
                # Due to race conditions, some jobs might have transitioned back to FAILED,
                # or a worker might still be holding it in memory, but our check inside _process_batch
                # guarantees they will abort before Qdrant write.
                # Here we wait for workers to crash gracefully.
                await asyncio.sleep(2)
                
                # Check if there are any jobs still claiming to be active
                count_stmt = select(RepoIndexJob).where(
                    RepoIndexJob.organization_id == organization_id,
                    RepoIndexJob.status.in_([JobStatus.CLONING, JobStatus.PARSING, JobStatus.ANALYZING, JobStatus.EMBEDDING, JobStatus.STORING])
                )
                active_jobs = (await db.scalars(count_stmt)).all()
                if not active_jobs:
                    quiescent = True
                    break

            if not quiescent:
                logger.error(f"Organization {organization_id} did not quiesce in time.")
                raise Exception("Failed to quiesce active jobs before timeout.")

            # Step 4: Qdrant Cleanup
            logger.info(f"Deleting Qdrant vectors for organization {organization_id}...")
            vector_store.delete_organization_vectors(str(organization_id))

            # Step 5: Notify Users & PostgreSQL Cleanup
            # Fetch all members to notify them
            logger.info(f"Notifying members of organization {org.name} about deletion...")
            member_stmt = select(OrganizationMember).where(OrganizationMember.organization_id == organization_id)
            members = (await db.scalars(member_stmt)).all()
            
            notifications = []
            for member in members:
                notifications.append(
                    Notification(
                        recipient_user_id=member.user_id,
                        organization_id=None,  # Must be None so it survives the cascade delete
                        type=NotificationType.SYSTEM_ALERT,
                        priority=NotificationPriority.WARNING,
                        title=f"Organization Deleted",
                        message=f"The organization '{org.name}' has been permanently deleted. Please contact your admin if you have questions.",
                        is_read=False,
                    )
                )
            
            if notifications:
                db.add_all(notifications)
                # Flush the notifications so they get saved before the cascade delete destroys the members
                await db.flush()

            # SQLAlchemy CASCADE handles the dependency tree automatically.
            logger.info(f"Deleting PostgreSQL records for organization {organization_id}...")
            await db.delete(org)
            await db.commit()
            
            logger.info(f"Successfully deleted organization {organization_id}.")
            return {"status": "SUCCESS"}

    try:
        return _run_async(_execute())
    except Exception as e:
        logger.error(f"Failed to delete organization {organization_id}: {e}")
        raise self.retry(exc=e, countdown=10)
