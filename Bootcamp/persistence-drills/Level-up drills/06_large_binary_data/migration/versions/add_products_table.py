
from alembic import op
import sqlalchemy as sa

revision = 'ghi789abc123'
down_revision = 'def456789abc'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'products',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('price', sa.Float(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name', name='uq_products_name')
    )
    op.create_index(op.f('ix_products_id'), 'products', ['id'], unique=False)

def downgrade():
    op.drop_table('products')