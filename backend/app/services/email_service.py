import abc
import aiosmtplib
from email.message import EmailMessage
from app.core.config import get_settings
import logging

settings = get_settings()
logger = logging.getLogger(__name__)

class EmailProvider(abc.ABC):
    @abc.abstractmethod
    async def send_email(self, to_email: str, subject: str, html_content: str) -> bool:
        pass

class SmtpEmailProvider(EmailProvider):
    async def send_email(self, to_email: str, subject: str, html_content: str) -> bool:
        # In development, always print the link to the console as a fallback
        if "localhost" in html_content:
            link_start = html_content.find('href="') + 6
            link_end = html_content.find('"', link_start)
            if link_start > 5 and link_end > link_start:
                extracted_link = html_content[link_start:link_end]
                logger.warning(f"DEVELOPMENT MODE: Click this link to continue: {extracted_link}")

        if not settings.SMTP_HOST or not settings.SMTP_USERNAME:
            logger.error("SMTP configuration is missing. Cannot send email.")
            return False
            
        message = EmailMessage()
        message["From"] = settings.EMAIL_FROM
        message["To"] = to_email
        message["Subject"] = subject
        message.set_content(html_content, subtype="html")
        
        try:
            await aiosmtplib.send(
                message,
                hostname=settings.SMTP_HOST,
                port=settings.SMTP_PORT,
                username=settings.SMTP_USERNAME,
                password=settings.SMTP_PASSWORD,
                start_tls=True if settings.SMTP_PORT == 587 else False,
            )
            return True
        except Exception as e:
            logger.error(f"Failed to send email via SMTP: {e}")
            return False

class EmailService:
    def __init__(self, provider: EmailProvider):
        self.provider = provider
        
    def _get_verify_template(self, name: str, link: str) -> str:
        return f"""
        <html>
            <body style="font-family: sans-serif; background-color: #09090b; color: #fff; padding: 40px; margin: 0;">
                <div style="max-width: 600px; margin: 0 auto; background-color: #18181b; padding: 40px; border-radius: 8px; border: 1px solid #27272a;">
                    <h1 style="color: #fff; margin-top: 0;">Welcome to ELARA, {name}!</h1>
                    <p style="color: #a1a1aa; font-size: 16px; line-height: 1.5;">Please verify your email address to activate your account and start using our platform.</p>
                    <br>
                    <a href="{link}" style="display: inline-block; background-color: #3b82f6; color: white; padding: 12px 24px; text-decoration: none; border-radius: 6px; font-weight: bold;">Verify Email</a>
                    <br><br><br>
                    <p style="color: #71717a; font-size: 14px;">If the button doesn't work, copy and paste this link into your browser:<br>
                    <a href="{link}" style="color: #3b82f6; word-break: break-all;">{link}</a></p>
                </div>
            </body>
        </html>
        """

    def _get_reset_template(self, name: str, link: str) -> str:
        return f"""
        <html>
            <body style="font-family: sans-serif; background-color: #09090b; color: #fff; padding: 40px; margin: 0;">
                <div style="max-width: 600px; margin: 0 auto; background-color: #18181b; padding: 40px; border-radius: 8px; border: 1px solid #27272a;">
                    <h1 style="color: #fff; margin-top: 0;">Password Reset</h1>
                    <p style="color: #a1a1aa; font-size: 16px; line-height: 1.5;">Hi {name},<br><br>You requested a password reset for your ELARA account. Click the button below to securely choose a new password.</p>
                    <br>
                    <a href="{link}" style="display: inline-block; background-color: #3b82f6; color: white; padding: 12px 24px; text-decoration: none; border-radius: 6px; font-weight: bold;">Reset Password</a>
                    <br><br><br>
                    <p style="color: #71717a; font-size: 14px;">If you didn't request this, you can safely ignore this email.</p>
                </div>
            </body>
        </html>
        """

    async def send_verification_email(self, to_email: str, name: str, token: str) -> bool:
        # Assuming frontend is on localhost:3000 for development
        link = f"http://localhost:3000/auth/verify-email/{token}"
        html_content = self._get_verify_template(name, link)
        return await self.provider.send_email(to_email, "Verify your ELARA account", html_content)

    async def send_password_reset_email(self, to_email: str, name: str, token: str) -> bool:
        link = f"http://localhost:3000/auth/reset-password/{token}"
        html_content = self._get_reset_template(name, link)
        return await self.provider.send_email(to_email, "Reset your ELARA password", html_content)

    def _get_org_invite_template(self, org_name: str, link: str) -> str:
        return f"""
        <html>
            <body style="font-family: sans-serif; background-color: #09090b; color: #fff; padding: 40px; margin: 0;">
                <div style="max-width: 600px; margin: 0 auto; background-color: #18181b; padding: 40px; border-radius: 8px; border: 1px solid #27272a;">
                    <h1 style="color: #fff; margin-top: 0;">You've been invited to {org_name}</h1>
                    <p style="color: #a1a1aa; font-size: 16px; line-height: 1.5;">You have been invited to join the <strong>{org_name}</strong> organization on ELARA.</p>
                    <br>
                    <a href="{link}" style="display: inline-block; background-color: #3b82f6; color: white; padding: 12px 24px; text-decoration: none; border-radius: 6px; font-weight: bold;">Accept Invitation</a>
                    <br><br><br>
                    <p style="color: #71717a; font-size: 14px;">If you didn't expect this invitation, you can safely ignore this email.</p>
                </div>
            </body>
        </html>
        """

    async def send_organization_invitation_email(self, to_email: str, org_name: str, token: str) -> bool:
        link = f"http://localhost:3000/organizations/invite/{token}"
        html_content = self._get_org_invite_template(org_name, link)
        return await self.provider.send_email(to_email, f"Invitation to join {org_name} on ELARA", html_content)

# Initialize the concrete provider
_provider = SmtpEmailProvider()
email_service = EmailService(provider=_provider)

