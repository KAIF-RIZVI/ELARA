"""enforce_one_personal_workspace_per_account

Revision ID: c153883542eb
Revises: ea36ca21aa2b
Create Date: 2026-08-28 15:45:01.103243

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c153883542eb'
down_revision: Union[str, Sequence[str], None] = 'ea36ca21aa2b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('workspaces', sa.Column('owner_id', sa.UUID(), nullable=True))
    op.create_index(op.f('ix_workspaces_owner_id'), 'workspaces', ['owner_id'], unique=False)
    op.create_foreign_key('fk_workspaces_owner_id_users', 'workspaces', 'users', ['owner_id'], ['id'], ondelete='CASCADE')
    
    # Backfill owner_id for personal workspaces using workspace_members
    op.execute("""
        UPDATE workspaces w
        SET owner_id = wm.user_id
        FROM workspace_members wm
        WHERE wm.workspace_id = w.id 
          AND wm.role = 'OWNER' 
          AND w.organization_id IS NULL
    """)

    # Create partial unique index to enforce 1 personal workspace per account
    op.execute("""
        CREATE UNIQUE INDEX ix_workspaces_personal_owner 
        ON workspaces (owner_id) 
        WHERE organization_id IS NULL
    """)


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DROP INDEX IF EXISTS ix_workspaces_personal_owner")
    op.drop_constraint('fk_workspaces_owner_id_users', 'workspaces', type_='foreignkey')
    op.drop_index(op.f('ix_workspaces_owner_id'), table_name='workspaces')
    op.drop_column('workspaces', 'owner_id')
