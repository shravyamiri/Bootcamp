"""Create e-commerce schema

Revision ID: xyz123456789
Revises:
Create Date: 2025-05-14 14:00:00

"""
from alembic import op
import sqlalchemy as sa

revision = 'xyz123456789'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Create users table
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(length=50), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.current_timestamp()),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username', name='uq_users_username'),
        sa.UniqueConstraint('email', name='uq_users_email')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)

    # Create products table
    op.create_table(
        'products',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('price', sa.DECIMAL(10, 2), nullable=False),
        sa.Column('stock', sa.Integer(), nullable=False),
        sa.CheckConstraint('stock >= 0', name='ck_products_stock_non_negative'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name', name='uq_products_name')
    )
    op.create_index(op.f('ix_products_id'), 'products', ['id'], unique=False)

    # Create orders table
    op.create_table(
        'orders',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('product_id', sa.Integer(), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.Column('order_date', sa.DateTime(), nullable=False, server_default=sa.func.current_timestamp()),
        sa.CheckConstraint('quantity > 0', name='ck_orders_quantity_positive'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_orders_user_id'),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], name='fk_orders_product_id'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_orders_id'), 'orders', ['id'], unique=False)

def downgrade():
    op.drop_table('orders')
    op.drop_table('products')
    op.drop_table('users')