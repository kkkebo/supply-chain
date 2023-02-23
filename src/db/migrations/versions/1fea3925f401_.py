"""empty message

Revision ID: 1fea3925f401
Revises: 
Create Date: 2023-02-23 18:47:14.458682

"""
import json
import os

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fea3925f401'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    users = op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=False),
    sa.Column('password_hashed', sa.String(length=255), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('modified_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('modified_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['modified_by'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    op.add_column(
        "users",
        sa.Column(
            "role", sa.Enum('admin', 'viewer', name='role'), nullable=True
        ),
    )
    with open(
            os.path.join(os.path.dirname(__file__), "../data/users.json")
    ) as f:
        user_data = f.read()

    op.bulk_insert(users, json.loads(user_data))

    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('modified_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('modified_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['modified_by'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_products_id'), 'products', ['id'], unique=False)
    op.create_table('tanks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('max_capacity', sa.Float(), nullable=False),
    sa.Column('current_capacity', sa.Float(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('modified_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('modified_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['modified_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tanks_id'), 'tanks', ['id'], unique=False)
    op.create_table('operations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mass', sa.Float(), nullable=False),
    sa.Column('date_start', sa.DateTime(), nullable=False),
    sa.Column('date_end', sa.DateTime(), nullable=False),
    sa.Column('tank_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('modified_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('modified_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['modified_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['tank_id'], ['tanks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_operations_id'), 'operations', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_operations_id'), table_name='operations')
    op.drop_table('operations')
    op.drop_index(op.f('ix_tanks_id'), table_name='tanks')
    op.drop_table('tanks')
    op.drop_index(op.f('ix_products_id'), table_name='products')
    op.drop_table('products')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###