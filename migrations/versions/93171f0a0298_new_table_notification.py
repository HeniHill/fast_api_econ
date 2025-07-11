"""New Table Notification

Revision ID: 93171f0a0298
Revises: 4cd45bf93f6d
Create Date: 2024-11-13 12:20:56.985741

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '93171f0a0298'
down_revision: Union[str, None] = '4cd45bf93f6d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notification',
    sa.Column('id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('type', sqlmodel.sql.sqltypes.AutoString(length=191), nullable=False),
    sa.Column('notifiable_type', sqlmodel.sql.sqltypes.AutoString(length=191), nullable=False),
    sa.Column('notifiable_id', sa.Integer(), nullable=False),
    sa.Column('data', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('read_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('notification')
    # ### end Alembic commands ###
