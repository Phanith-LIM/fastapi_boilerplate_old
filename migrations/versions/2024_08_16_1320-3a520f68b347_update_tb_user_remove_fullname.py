"""update Tb_User remove fullname

Revision ID: 3a520f68b347
Revises: 225dbf954167
Create Date: 2024-08-16 13:20:46.093263

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3a520f68b347'
down_revision: Union[str, None] = '225dbf954167'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'fullname')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('fullname', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
