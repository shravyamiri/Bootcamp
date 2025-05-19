"""Add email_history table

Revision ID: jkl012def456
Revises: ghi789abc123
Create Date: 2025-05-14 00:00:00

"""
from alembic import op
import sqlalchemy as sa

revision = 'jkl012def456'
down_revision = 'ghi789abc123'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'email_history',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('changed_at', sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_email_history_user_id'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_email_history_id'), 'email_history', ['id'], unique=False)

def downgrade():
    op.drop_table('email_history')