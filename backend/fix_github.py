import asyncio
import jwt
import time
import httpx
from datetime import datetime, timezone
import uuid
import os

from sqlalchemy import select
from app.core.database import AsyncSessionLocal
from app.models.organization import Organization
from app.models.integrations import GitHubIntegration, IntegrationStatus
from app.core.config import get_settings

settings = get_settings()

async def fix_github():
    print("=== GitHub App Auto-Fixer ===")
    
    # 1. Generate JWT for the App
    now = int(time.time())
    payload = {
        "iat": now - 60,
        "exp": now + (10 * 60),
        "iss": settings.GITHUB_APP_ID
    }
    
    try:
        encoded_jwt = jwt.encode(payload, settings.GITHUB_APP_PRIVATE_KEY, algorithm="RS256")
    except Exception as e:
        print(f"Failed to generate JWT: {e}")
        return

    # 2. Get all installations for this App
    print("Fetching installations from GitHub...")
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.github.com/app/installations",
            headers={
                "Authorization": f"Bearer {encoded_jwt}",
                "Accept": "application/vnd.github.v3+json",
                "User-Agent": "ELARA-App"
            }
        )
        
        if response.status_code != 200:
            print(f"Failed to fetch installations: {response.text}")
            return
            
        installations = response.json()
        
    if not installations:
        print("No installations found on GitHub! The user really does need to install the app.")
        return
        
    print(f"Found {len(installations)} installations.")
    
    # Grab the first installation (assuming this is a single-tenant dev environment for now)
    installation = installations[0]
    installation_id = str(installation["id"])
    account_login = installation["account"]["login"]
    account_id = str(installation["account"]["id"])
    print(f"Using installation: {installation_id} for account {account_login}")
    
    # 3. Link it in the database
    async with AsyncSessionLocal() as db:
        # Find all user organizations
        orgs = await db.execute(select(Organization))
        orgs_list = orgs.scalars().all()
        
        if not orgs_list:
            print("No organizations found in database.")
            return
            
        for org in orgs_list:
            print(f"Linking to organization: {org.name} ({org.id})")
            
            # Check if integration exists
            stmt = select(GitHubIntegration).where(GitHubIntegration.organization_id == org.id)
            result = await db.execute(stmt)
            integration = result.scalar_one_or_none()
            
            if not integration:
                integration = GitHubIntegration(
                    organization_id=org.id,
                    provider="github",
                    github_installation_id=installation_id,
                    github_account_id=account_id,
                    github_account_login=account_login,
                    status=IntegrationStatus.CONNECTED,
                    installed_at=datetime.now(timezone.utc),
                    last_verified_at=datetime.now(timezone.utc)
                )
                db.add(integration)
                print("Created new GitHubIntegration record.")
            else:
                integration.github_installation_id = installation_id
                integration.github_account_id = account_id
                integration.github_account_login = account_login
                integration.status = IntegrationStatus.CONNECTED
                print("Updated existing GitHubIntegration record.")
                
        await db.commit()
        print("SUCCESS! The GitHub App is now linked in the database.")

if __name__ == "__main__":
    asyncio.run(fix_github())
