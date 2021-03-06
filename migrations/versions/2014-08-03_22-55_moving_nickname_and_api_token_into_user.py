"""Moving nickname and API token into User

Revision ID: 37f87b01afe3
Revises: 18a06a1308ae
Create Date: 2014-08-03 22:55:41.787681

"""

# revision identifiers, used by Alembic.
revision = '37f87b01afe3'
down_revision = '18a06a1308ae'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('admiral', 'nickname')
    op.drop_column('admiral', 'api_token')
    op.add_column('user', sa.Column('api_token', sa.String(length=40), nullable=True))
    op.add_column('user', sa.Column('nickname', sa.String(length=255), nullable=True))
    op.create_unique_constraint(None, 'user', ['nickname'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user')
    op.drop_column('user', 'nickname')
    op.drop_column('user', 'api_token')
    op.add_column('admiral', sa.Column('api_token', sa.VARCHAR(length=40), autoincrement=False, nullable=True))
    op.add_column('admiral', sa.Column('nickname', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    ### end Alembic commands ###
