import os
import uuid
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from typing import AsyncGenerator
from sqlalchemy.pool import NullPool

from app.main import app
from app.core.base_model import Base
from app.api.deps import get_db, get_current_user

from app.models.identity import User, WorkspaceMember, MemberRole
from app.models.organization import Organization, OrganizationMember, OrganizationRole
from app.models.workspace import Workspace
from app.models.bug import Bug, BugState, BugPriority

from app.core.config import get_settings
settings = get_settings()
TEST_DATABASE_URL = settings.SQLALCHEMY_DATABASE_URI.rsplit('/', 1)[0] + '/elara_test'

engine = create_async_engine(TEST_DATABASE_URL, echo=False, poolclass=NullPool)
TestingSessionLocal = async_sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession, expire_on_commit=False
)

async def override_get_db() -> AsyncGenerator[AsyncSession, None]:
    async with TestingSessionLocal() as session:
        yield session

app.dependency_overrides[get_db] = override_get_db

@pytest_asyncio.fixture(autouse=True)
async def create_test_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest_asyncio.fixture
async def db() -> AsyncGenerator[AsyncSession, None]:
    async with TestingSessionLocal() as session:
        yield session

@pytest_asyncio.fixture
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        yield client

@pytest_asyncio.fixture
async def test_user(db: AsyncSession) -> User:
    user = User(id=uuid.uuid4(), email="test@example.com", full_name="Test User", is_active=True)
    db.add(user)
    await db.commit()
    return user

@pytest_asyncio.fixture
async def test_other_user(db: AsyncSession) -> User:
    user = User(id=uuid.uuid4(), email="other@example.com", full_name="Other User", is_active=True)
    db.add(user)
    await db.commit()
    return user

@pytest_asyncio.fixture
def auth_client(async_client: AsyncClient, test_user: User):
    app.dependency_overrides[get_current_user] = lambda: test_user
    yield async_client
    app.dependency_overrides.pop(get_current_user, None)

@pytest_asyncio.fixture
def other_auth_client(async_client: AsyncClient, test_other_user: User):
    app.dependency_overrides[get_current_user] = lambda: test_other_user
    yield async_client
    app.dependency_overrides.pop(get_current_user, None)

@pytest_asyncio.fixture
async def test_org(db: AsyncSession, test_user: User) -> Organization:
    org = Organization(id=uuid.uuid4(), name="Test Org", slug="test-org", owner_id=test_user.id)
    db.add(org)
    await db.commit()
    org_member = OrganizationMember(organization_id=org.id, user_id=test_user.id, role=OrganizationRole.OWNER, status="ACTIVE")
    db.add(org_member)
    await db.commit()
    return org

@pytest_asyncio.fixture
async def test_workspace(db: AsyncSession, test_user: User, test_org: Organization) -> Workspace:
    ws = Workspace(id=uuid.uuid4(), name="Test WS", slug="test-ws", organization_id=test_org.id, created_by=test_user.id)
    db.add(ws)
    await db.commit()
    ws_member = WorkspaceMember(workspace_id=ws.id, user_id=test_user.id, role=MemberRole.ADMIN)
    db.add(ws_member)
    await db.commit()
    return ws
@pytest_asyncio.fixture
async def other_org(db: AsyncSession, test_other_user: User) -> Organization:
    org = Organization(id=uuid.uuid4(), name="Other Org", slug="other-org", owner_id=test_other_user.id)
    db.add(org)
    await db.commit()
    org_member = OrganizationMember(organization_id=org.id, user_id=test_other_user.id, role=OrganizationRole.OWNER, status="ACTIVE")
    db.add(org_member)
    await db.commit()
    return org

@pytest_asyncio.fixture
async def other_workspace(db: AsyncSession, test_other_user: User, other_org: Organization) -> Workspace:
    ws = Workspace(id=uuid.uuid4(), name="Other WS", slug="other-ws", organization_id=other_org.id, created_by=test_other_user.id)
    db.add(ws)
    await db.commit()
    ws_member = WorkspaceMember(workspace_id=ws.id, user_id=test_other_user.id, role=MemberRole.ADMIN)
    db.add(ws_member)
    await db.commit()
    return ws

@pytest_asyncio.fixture
async def legacy_workspace(db: AsyncSession, test_user: User) -> Workspace:
    ws = Workspace(id=uuid.uuid4(), name="Legacy WS", slug="legacy-ws", organization_id=None, created_by=test_user.id)
    db.add(ws)
    await db.commit()
    ws_member = WorkspaceMember(workspace_id=ws.id, user_id=test_user.id, role=MemberRole.ADMIN)
    db.add(ws_member)
    await db.commit()
    return ws
