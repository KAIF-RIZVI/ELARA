import asyncio
from app.services.email_service import SmtpEmailProvider
from app.core.config import get_settings

async def test():
    settings = get_settings()
    print(f"SMTP Host: {settings.SMTP_HOST}")
    print(f"SMTP User: {settings.SMTP_USERNAME}")
    print(f"SMTP Pass: {settings.SMTP_PASSWORD}")
    
    provider = SmtpEmailProvider()
    print("Sending test email...")
    result = await provider.send_email(
        to_email=settings.SMTP_USERNAME,
        subject="ELARA Test Email",
        html_content="<h1>This is a test email</h1>"
    )
    print(f"Result: {result}")

if __name__ == "__main__":
    asyncio.run(test())
