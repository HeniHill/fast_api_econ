"""New Table Order and Main Order New

Revision ID: 03c04d532e99
Revises: 914219127156
Create Date: 2024-11-13 09:45:12.899130

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '03c04d532e99'
down_revision: Union[str, None] = '914219127156'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('color',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('colour_name', sqlmodel.sql.sqltypes.AutoString(length=191), nullable=False),
    sa.Column('hex', sqlmodel.sql.sqltypes.AutoString(length=191), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mainorder',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('unique_bank_code', sqlmodel.sql.sqltypes.AutoString(length=191), nullable=True),
    sa.Column('order_code', sqlmodel.sql.sqltypes.AutoString(length=191), nullable=False),
    sa.Column('total_price', sa.Float(), nullable=False),
    sa.Column('discount_price', sa.Float(), nullable=False),
    sa.Column('delivery_price', sa.Float(), nullable=False),
    sa.Column('delivery_method', sqlmodel.sql.sqltypes.AutoString(length=191), nullable=False),
    sa.Column('payment_method', sqlmodel.sql.sqltypes.AutoString(length=191), nullable=False),
    sa.Column('vendor_delivery_confirmation', sa.Boolean(), nullable=False),
    sa.Column('customer_delivery_confirmation', sa.Boolean(), nullable=False),
    sa.Column('payment_status', sa.Boolean(), nullable=False),
    sa.Column('order_pin', sqlmodel.sql.sqltypes.AutoString(length=191), nullable=False),
    sa.Column('deliveryp_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mainorder')
    op.drop_table('color')
    # ### end Alembic commands ###
