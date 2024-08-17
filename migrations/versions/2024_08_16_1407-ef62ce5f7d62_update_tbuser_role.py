"""update Tbuser role

Revision ID: ef62ce5f7d62
Revises: 68ac26cd5bb9
Create Date: 2024-08-16 14:07:37.675994

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'ef62ce5f7d62'
down_revision: Union[str, None] = '68ac26cd5bb9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('roles', postgresql.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'roles')
    # ### end Alembic commands ###
