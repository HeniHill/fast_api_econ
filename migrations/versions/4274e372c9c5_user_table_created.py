"""User Table created

Revision ID: 4274e372c9c5
Revises: 8cc44d2165c3
Create Date: 2024-11-07 14:04:19.505626

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '4274e372c9c5'
down_revision: Union[str, None] = '8cc44d2165c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('activation', sa.Integer(), nullable=False),
    sa.Column('role', sa.Integer(), nullable=False),
    sa.Column('email_verified_at', sa.DateTime(), nullable=False),
    sa.Column('password', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('photo_url', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('image_version', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('shop_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('phone_number', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('phone_number2', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('phone_number3', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('about_shop', sa.Integer(), nullable=False),
    sa.Column('credit', sa.Boolean(), nullable=False),
    sa.Column('tin', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('business_type', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('remember_token', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('api')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('api',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('url', mysql.VARCHAR(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('user')
    # ### end Alembic commands ###
