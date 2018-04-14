"""empty message

Revision ID: c21ddd7274c
Revises: 51bc7b650f42
Create Date: 2015-05-09 18:20:33.229000

"""

# revision identifiers, used by Alembic.
revision = 'c21ddd7274c'
down_revision = '51bc7b650f42'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    ### end Alembic commands ###
