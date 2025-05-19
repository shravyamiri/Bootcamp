
from alembic import op
import sqlalchemy as sa

revision = 'def456789abc'
down_revision = 'abc123456789'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('users',
        sa.Column('email', sa.String(), nullable=False,
                 server_default='default@example.com')
    )
    op.create_unique_constraint('uq_users_email', 'users', ['email'])
    op.alter_column('users', 'email', server_default=None)

def downgrade():
    op.drop_constraint('uq_users_email', 'users', type_='unique')
    op.drop_column('users', 'email')