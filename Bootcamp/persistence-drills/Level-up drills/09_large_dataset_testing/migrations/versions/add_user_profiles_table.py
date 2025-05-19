
from alembic import op
import sqlalchemy as sa

revision = 'pqr678jkl012'
down_revision = 'mno345ghi789'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'user_profiles',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('image_blob', sa.LargeBinary(), nullable=True),
        sa.Column('image_path', sa.String(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_user_profiles_user_id'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('user_id', name='uq_user_profiles_user_id')
    )
    op.create_index(op.f('ix_user_profiles_id'), 'user_profiles', ['id'], unique=False)

def downgrade():
    op.drop_table('user_profiles')