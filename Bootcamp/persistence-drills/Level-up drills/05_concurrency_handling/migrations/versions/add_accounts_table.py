
from alembic import op
import sqlalchemy as sa

revision = 'mno345ghi789'
down_revision = 'jkl012def456'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'accounts',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('balance', sa.Float(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_accounts_id'), 'accounts', ['id'], unique=False)

def downgrade():
    op.drop_table('accounts')