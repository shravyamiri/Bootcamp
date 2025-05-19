
from alembic import op
import sqlalchemy as sa

revision = 'abc123456789'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('users',
        sa.Column('created_at', sa.DateTime(), nullable=False,
                 server_default=sa.func.now())
    )
    op.alter_column('users', 'created_at', server_default=None)

def downgrade():
    op.drop_column('users', 'created_at')