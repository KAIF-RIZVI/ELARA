"""Decouple Canonical Workspaces

Revision ID: 6ff1eb8db7fc
Revises: c153883542eb
Create Date: 2026-08-28 23:09:34.545228

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '6ff1eb8db7fc'
down_revision: Union[str, Sequence[str], None] = 'c153883542eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    
    # Drop the unused old 'api_keys' table if it existed
    op.drop_table('api_keys')
    
    # Rename 'workspace_api_keys' to 'api_keys'
    op.rename_table('workspace_api_keys', 'api_keys')
    
    # Rename index too
    op.execute("ALTER INDEX ix_workspace_api_keys_key_hash RENAME TO ix_api_keys_key_hash")
    op.execute("ALTER INDEX ix_workspace_api_keys_organization_id RENAME TO ix_api_keys_organization_id")
    op.execute("ALTER INDEX ix_workspace_api_keys_workspace_id RENAME TO ix_api_keys_workspace_id")

    # 1. Update schema columns to nullable
    op.alter_column('bug_assignments', 'workspace_id', existing_type=sa.UUID(), nullable=True)
    op.alter_column('bug_assignments', 'organization_id', existing_type=sa.UUID(), nullable=True)
    op.alter_column('bug_comments', 'workspace_id', existing_type=sa.UUID(), nullable=True)
    op.alter_column('bug_comments', 'organization_id', existing_type=sa.UUID(), nullable=True)
    op.alter_column('bugs', 'organization_id', existing_type=sa.UUID(), nullable=True)
    op.alter_column('bugs', 'workspace_id', existing_type=sa.UUID(), nullable=True)
    op.alter_column('idempotency_keys', 'organization_id', existing_type=sa.UUID(), nullable=True)
    op.alter_column('idempotency_keys', 'workspace_id', existing_type=sa.UUID(), nullable=True)
    
    op.alter_column('api_keys', 'workspace_id', existing_type=sa.UUID(), nullable=True)
    op.alter_column('api_keys', 'organization_id', existing_type=sa.UUID(), nullable=True)
    
    # 2. Migrate data
    
    # For Canonical Workspaces (organization_id IS NOT NULL):
    conn.execute(sa.text("""
        UPDATE bugs 
        SET workspace_id = NULL
        FROM workspaces w 
        WHERE bugs.workspace_id = w.id AND w.organization_id IS NOT NULL
    """))
    
    conn.execute(sa.text("""
        UPDATE bug_assignments 
        SET workspace_id = NULL
        FROM workspaces w 
        WHERE bug_assignments.workspace_id = w.id AND w.organization_id IS NOT NULL
    """))

    conn.execute(sa.text("""
        UPDATE bug_comments 
        SET workspace_id = NULL
        FROM workspaces w 
        WHERE bug_comments.workspace_id = w.id AND w.organization_id IS NOT NULL
    """))

    conn.execute(sa.text("""
        UPDATE idempotency_keys 
        SET workspace_id = NULL
        FROM workspaces w 
        WHERE idempotency_keys.workspace_id = w.id AND w.organization_id IS NOT NULL
    """))
    
    conn.execute(sa.text("""
        UPDATE api_keys 
        SET workspace_id = NULL
        FROM workspaces w 
        WHERE api_keys.workspace_id = w.id AND w.organization_id IS NOT NULL
    """))

    # For Personal Workspaces (organization_id IS NULL):
    conn.execute(sa.text("""
        UPDATE bugs 
        SET organization_id = NULL
        FROM workspaces w 
        WHERE bugs.workspace_id = w.id AND w.organization_id IS NULL
    """))
    
    conn.execute(sa.text("""
        UPDATE bug_assignments 
        SET organization_id = NULL
        FROM workspaces w 
        WHERE bug_assignments.workspace_id = w.id AND w.organization_id IS NULL
    """))

    conn.execute(sa.text("""
        UPDATE bug_comments 
        SET organization_id = NULL
        FROM workspaces w 
        WHERE bug_comments.workspace_id = w.id AND w.organization_id IS NULL
    """))

    conn.execute(sa.text("""
        UPDATE idempotency_keys 
        SET organization_id = NULL
        FROM workspaces w 
        WHERE idempotency_keys.workspace_id = w.id AND w.organization_id IS NULL
    """))

    conn.execute(sa.text("""
        UPDATE api_keys 
        SET organization_id = NULL
        FROM workspaces w 
        WHERE api_keys.workspace_id = w.id AND w.organization_id IS NULL
    """))
    
    conn.execute(sa.text("""
        UPDATE activity_logs
        SET workspace_id = NULL, organization_id = w.organization_id
        FROM workspaces w
        WHERE activity_logs.workspace_id = w.id AND w.organization_id IS NOT NULL
    """))

    # Now we can safely delete canonical workspaces
    conn.execute(sa.text("""
        DELETE FROM workspaces WHERE organization_id IS NOT NULL
    """))
    
    # 4. Check constraints
    op.create_check_constraint('chk_bug_owner', 'bugs', '(workspace_id IS NULL) <> (organization_id IS NULL)')
    op.create_check_constraint('chk_bug_assignment_owner', 'bug_assignments', '(workspace_id IS NULL) <> (organization_id IS NULL)')
    op.create_check_constraint('chk_bug_comment_owner', 'bug_comments', '(workspace_id IS NULL) <> (organization_id IS NULL)')
    op.create_check_constraint('chk_idempotency_owner', 'idempotency_keys', '(workspace_id IS NULL) <> (organization_id IS NULL)')
    op.create_check_constraint('chk_apikey_owner', 'api_keys', '(workspace_id IS NULL) <> (organization_id IS NULL)')
    
    # Unique constraints
    op.drop_constraint('uix_workspace_id_key', 'idempotency_keys', type_='unique')
    op.create_unique_constraint('uix_workspace_org_key', 'idempotency_keys', ['workspace_id', 'organization_id', 'key'])
    
    # Drop index that is no longer valid
    op.drop_index('ix_workspaces_personal_owner', table_name='workspaces', postgresql_where='(organization_id IS NULL)')


def downgrade() -> None:
    pass
