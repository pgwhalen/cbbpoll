"""Add redditUrl column to poll

Revision ID: 7ceaa5c9096
Revises: 47266dd94e01
Create Date: 2014-10-26 17:42:40.618616

"""

# revision identifiers, used by Alembic.
revision = '7ceaa5c9096'
down_revision = '47266dd94e01'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('poll', sa.Column('redditUrl', sa.String(length=2083), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('poll', 'redditUrl')
    ### end Alembic commands ###
