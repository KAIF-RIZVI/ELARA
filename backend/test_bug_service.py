import pytest
import uuid
import datetime
from unittest.mock import AsyncMock, MagicMock

from app.services.bug import bug_service, VALID_TRANSITIONS
from app.models.bug import Bug, BugState, BugPriority, BugSeverity
from app.schemas.bug import BugCreate, BugUpdate, BugStatusUpdate, BugPriorityUpdate, BugAssignUpdate
from app.models.workspace import Workspace, ActivityLog
from app.models.identity import WorkspaceMember

import contextlib

@pytest.fixture
def mock_session():
    session = AsyncMock()
    
    @contextlib.asynccontextmanager
    async def begin_nested_mock():
        yield AsyncMock()
        
    session.begin_nested = begin_nested_mock
    return session

@pytest.fixture
def base_uuids():
    return {
        "org_id": uuid.uuid4(),
        "workspace_id": uuid.uuid4(),
        "user_id": uuid.uuid4(),
        "bug_id": uuid.uuid4()
    }

@pytest.mark.asyncio
async def test_create_bug_success(mock_session, base_uuids):
    mock_workspace = Workspace(id=base_uuids["workspace_id"], organization_id=base_uuids["org_id"])
    mock_session.scalar.return_value = mock_workspace

    obj_in = BugCreate(title="Test Bug", description="Test Desc")
    
    bug = await bug_service.create_bug(
        mock_session,
        obj_in=obj_in,
        organization_id=base_uuids["org_id"],
        workspace_id=base_uuids["workspace_id"],
        user_id=base_uuids["user_id"]
    )
    
    assert bug.title == "Test Bug"
    assert bug.state == BugState.OPEN
    assert bug.priority == BugPriority.P2
    mock_session.add.assert_called()
    mock_session.commit.assert_called_once()
    
    # Check activity log was added
    add_calls = mock_session.add.call_args_list
    assert len(add_calls) == 2
    assert isinstance(add_calls[1][0][0], ActivityLog)
    assert add_calls[1][0][0].action == "BUG_CREATED"

@pytest.mark.asyncio
async def test_legacy_workspace_rejection(mock_session, base_uuids):
    # Workspace has None organization_id
    mock_workspace = Workspace(id=base_uuids["workspace_id"], organization_id=None)
    mock_session.scalar.return_value = mock_workspace

    obj_in = BugCreate(title="Test Bug", description="Test Desc")
    
    with pytest.raises(ValueError, match="Legacy workspaces without an organization cannot create bugs"):
        await bug_service.create_bug(
            mock_session,
            obj_in=obj_in,
            organization_id=base_uuids["org_id"],
            workspace_id=base_uuids["workspace_id"],
            user_id=base_uuids["user_id"]
        )

@pytest.mark.asyncio
async def test_cross_tenant_isolation_creation(mock_session, base_uuids):
    # Workspace belongs to a different org
    mock_workspace = Workspace(id=base_uuids["workspace_id"], organization_id=uuid.uuid4())
    mock_session.scalar.return_value = mock_workspace

    obj_in = BugCreate(title="Test Bug", description="Test Desc")
    
    with pytest.raises(ValueError, match="Workspace does not belong to the authorized organization"):
        await bug_service.create_bug(
            mock_session,
            obj_in=obj_in,
            organization_id=base_uuids["org_id"],
            workspace_id=base_uuids["workspace_id"],
            user_id=base_uuids["user_id"]
        )

@pytest.mark.asyncio
async def test_get_bug_not_found(mock_session, base_uuids):
    mock_session.scalar.return_value = None
    bug = await bug_service.get_bug(
        mock_session, base_uuids["bug_id"], base_uuids["org_id"], base_uuids["workspace_id"]
    )
    assert bug is None

@pytest.mark.asyncio
async def test_valid_status_transition(mock_session, base_uuids):
    mock_bug = Bug(id=base_uuids["bug_id"], state=BugState.OPEN, title="Bug1")
    mock_session.scalar.return_value = mock_bug
    
    # Transition OPEN -> IN_PROGRESS is valid
    update_in = BugStatusUpdate(state=BugState.IN_PROGRESS)
    bug = await bug_service.change_status(
        mock_session,
        bug_id=base_uuids["bug_id"],
        obj_in=update_in,
        organization_id=base_uuids["org_id"],
        workspace_id=base_uuids["workspace_id"],
        user_id=base_uuids["user_id"]
    )
    
    assert bug.state == BugState.IN_PROGRESS
    mock_session.commit.assert_called_once()
    
    # Check activity log
    add_calls = mock_session.add.call_args_list
    assert len(add_calls) == 1
    assert add_calls[0][0][0].action == "STATUS_CHANGED"

@pytest.mark.asyncio
async def test_invalid_status_transition(mock_session, base_uuids):
    mock_bug = Bug(id=base_uuids["bug_id"], state=BugState.OPEN, title="Bug1")
    mock_session.scalar.return_value = mock_bug
    
    # Transition OPEN -> VERIFIED is invalid
    update_in = BugStatusUpdate(state=BugState.VERIFIED)
    with pytest.raises(ValueError, match="Invalid state transition from OPEN to VERIFIED"):
        await bug_service.change_status(
            mock_session,
            bug_id=base_uuids["bug_id"],
            obj_in=update_in,
            organization_id=base_uuids["org_id"],
            workspace_id=base_uuids["workspace_id"],
            user_id=base_uuids["user_id"]
        )
    mock_session.commit.assert_not_called()

@pytest.mark.asyncio
async def test_unauthorized_mutation_rejection(mock_session, base_uuids):
    # scalar returns None when querying bug with proper tenant ID
    mock_session.scalar.return_value = None
    
    update_in = BugUpdate(title="New Title")
    with pytest.raises(ValueError, match="Bug not found or unauthorized"):
        await bug_service.update_bug(
            mock_session,
            bug_id=base_uuids["bug_id"],
            obj_in=update_in,
            organization_id=base_uuids["org_id"],
            workspace_id=base_uuids["workspace_id"],
            user_id=base_uuids["user_id"]
        )

@pytest.mark.asyncio
async def test_priority_change(mock_session, base_uuids):
    mock_bug = Bug(id=base_uuids["bug_id"], priority=BugPriority.P2, title="Bug1")
    mock_session.scalar.return_value = mock_bug
    
    update_in = BugPriorityUpdate(priority=BugPriority.P0)
    bug = await bug_service.change_priority(
        mock_session,
        bug_id=base_uuids["bug_id"],
        obj_in=update_in,
        organization_id=base_uuids["org_id"],
        workspace_id=base_uuids["workspace_id"],
        user_id=base_uuids["user_id"]
    )
    
    assert bug.priority == BugPriority.P0
    mock_session.commit.assert_called_once()
    assert mock_session.add.call_args_list[0][0][0].action == "PRIORITY_CHANGED"

@pytest.mark.asyncio
async def test_not_implemented_developer_assignment(mock_session, base_uuids):
    mock_bug = Bug(id=base_uuids["bug_id"])
    mock_session.scalar.return_value = mock_bug
    
    update_in = BugAssignUpdate(developer_id=uuid.uuid4())
    with pytest.raises(NotImplementedError, match="Missing assignee field"):
        await bug_service.assign_developer(
            mock_session,
            bug_id=base_uuids["bug_id"],
            obj_in=update_in,
            organization_id=base_uuids["org_id"],
            workspace_id=base_uuids["workspace_id"],
            user_id=base_uuids["user_id"]
        )

@pytest.mark.asyncio
async def test_not_implemented_deletion(mock_session, base_uuids):
    mock_bug = Bug(id=base_uuids["bug_id"])
    mock_session.scalar.return_value = mock_bug
    
    with pytest.raises(NotImplementedError, match="No explicit deletion strategy exists"):
        await bug_service.delete_bug(
            mock_session,
            bug_id=base_uuids["bug_id"],
            organization_id=base_uuids["org_id"],
            workspace_id=base_uuids["workspace_id"],
            user_id=base_uuids["user_id"]
        )
