"""Create Log Table

Revision ID: f4112876b51b
Revises: e93a286677ae
Create Date: 2024-11-20 17:34:28.646264

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'f4112876b51b'
down_revision: Union[str, None] = 'e93a286677ae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('logs', sa.Column('endpoint', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('logs', 'endpoint')
    # ### end Alembic commands ###
