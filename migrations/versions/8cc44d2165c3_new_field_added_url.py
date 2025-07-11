"""New field added [url]

Revision ID: 8cc44d2165c3
Revises: 1c6bf8057311
Create Date: 2024-11-07 13:30:06.783740

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '8cc44d2165c3'
down_revision: Union[str, None] = '1c6bf8057311'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('api', sa.Column('url', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('api', 'url')
    # ### end Alembic commands ###
