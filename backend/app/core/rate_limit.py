from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from app.core.config import get_settings

settings = get_settings()

if settings.ENVIRONMENT == "production":
    limiter = Limiter(key_func=get_remote_address, storage_uri=settings.REDIS_URL)
else:
    limiter = Limiter(key_func=get_remote_address)