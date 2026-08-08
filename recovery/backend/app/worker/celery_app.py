from celery import Celery
from app.core.config import get_settings

settings = get_settings()

celery_app = Celery(
    "elara_worker",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
    worker_prefetch_multiplier=1,
)

# Autodiscover tasks in the tasks module
celery_app.autodiscover_tasks(["app.worker"])