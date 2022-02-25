"""Add block_behaviour setting for user

Revision ID: 9282e982bc05
Revises: 07b870d7cc86
Create Date: 2022-02-18 12:37:55.707424

"""
import sqlalchemy_utils
from sqlalchemy.dialects import postgresql
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9282e982bc05'
down_revision = '07b870d7cc86'
branch_labels = None
depends_on = None

def __create_enum() -> postgresql.ENUM:
    return postgresql.ENUM('return_2xx', 'return_5xx', name='block_behaviour_enum')

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    block_behaviour_enum = __create_enum()
    block_behaviour_enum.create(op.get_bind())

    op.add_column('users', sa.Column('block_behaviour', block_behaviour_enum, nullable=False, default='return_2xx', server_default='return_2xx'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'block_behaviour')

    block_behaviour_enum = __create_enum()
    block_behaviour_enum.drop(op.get_bind())
    # ### end Alembic commands ###