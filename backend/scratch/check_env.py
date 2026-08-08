from app.core.config import get_settings

settings = get_settings()
print(f"SMTP_HOST: {settings.SMTP_HOST}")
print(f"SMTP_USERNAME: {settings.SMTP_USERNAME}")
print(f"SMTP_PASSWORD: {settings.SMTP_PASSWORD}")
print(f"EMAIL_FROM: {settings.EMAIL_FROM}")
