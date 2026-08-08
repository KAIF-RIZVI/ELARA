from sqlalchemy.ext.asyncio import AsyncSession
from app.core.base_service import BaseService
from app.models.identity import User, OAuthAccount, WorkspaceMember, MemberRole, MemberStatus
from app.models.workspace import Workspace, WorkspaceStatus, Subscription, PlanTier, AIWallet
from app.repositories.user import RepositoryUser, user as user_repo
from app.core.security import get_password_hash
import uuid
from datetime import datetime, timezone

class UserService(BaseService[User, RepositoryUser]):
    async def get_by_oauth(self, db: AsyncSession, provider: str, provider_user_id: str) -> User | None:
        return await self.repository.get_by_oauth(db, provider, provider_user_id)

    async def create_user(
        self, db: AsyncSession, *, email: str, full_name: str, 
        password: str | None = None, auth_provider: str = "google",
        provider_user_id: str | None = None
    ) -> User:
        # Check if email exists
        existing = await self.repository.get_by_email(db, email)
        if existing:
            raise ValueError(f"User with email {email} already exists.")
        
        # 1. Create User
        user = User(
            email=email,
            full_name=full_name,
            password_hash=get_password_hash(password) if password else None
        )
        db.add(user)
        await db.flush() # flush to get user.id
        
        # 2. Create OAuthAccount if provider_user_id is provided
        if provider_user_id:
            oauth_account = OAuthAccount(
                user_id=user.id,
                provider=auth_provider,
                provider_user_id=provider_user_id,
                email=email
            )
            db.add(oauth_account)
            
        # 3. Create Default Workspace
        slug = f"{full_name.lower().replace(' ', '-')}-{str(uuid.uuid4())[:8]}"
        workspace = Workspace(
            name=f"{full_name}'s Workspace",
            slug=slug,
            status=WorkspaceStatus.ACTIVE,
            settings={}
        )
        db.add(workspace)
        await db.flush() # get workspace.id
        
        # 4. Create Workspace Membership
        member = WorkspaceMember(
            workspace_id=workspace.id,
            user_id=user.id,
            role=MemberRole.OWNER,
            status=MemberStatus.ACTIVE,
            joined_at=datetime.now(timezone.utc)
        )
        db.add(member)
        
        # 5. Create Default Subscription
        subscription = Subscription(
            workspace_id=workspace.id,
            plan=PlanTier.FREE,
            status="active"
        )
        db.add(subscription)
        
        # 6. Create AI Wallet
        wallet = AIWallet(
            workspace_id=workspace.id,
            balance_units=1000, # 1000 free units
            monthly_grant=1000
        )
        db.add(wallet)
        
        await db.commit()
        await db.refresh(user)
        return user

user_service = UserService(repository=user_repo)
