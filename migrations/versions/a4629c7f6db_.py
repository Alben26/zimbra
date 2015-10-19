"""empty message

Revision ID: a4629c7f6db
Revises: 2f0814150031
Create Date: 2015-10-13 18:55:38.965246

"""

# revision identifiers, used by Alembic.
revision = 'a4629c7f6db'
down_revision = '2f0814150031'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sqlite_sequence')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sqlite_sequence',
    sa.Column('name', sa.NullType(), nullable=True),
    sa.Column('seq', sa.NullType(), nullable=True)
    )
    ### end Alembic commands ###
