"""update Tb_User password

Revision ID: 27de0e2c835a
Revises: 0bcacf706c1d
Create Date: 2024-08-16 13:15:59.330806

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '27de0e2c835a'
down_revision: Union[str, None] = '0bcacf706c1d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('hashed_password', sa.String(), nullable=True))
    op.drop_column('users', 'hashedPassword')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('hashedPassword', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('users', 'hashed_password')
    # ### end Alembic commands ###