"""empty message

Revision ID: c065a4328066
Revises: 
Create Date: 2020-03-25 11:43:32.607479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c065a4328066'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('report',
    sa.Column('id', sa.String(length=2), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('flag', sa.String(length=120), nullable=True),
    sa.Column('reports', sa.Integer(), nullable=True),
    sa.Column('cases', sa.Integer(), nullable=True),
    sa.Column('deaths', sa.Integer(), nullable=True),
    sa.Column('recovered', sa.Integer(), nullable=True),
    sa.Column('lat', sa.Integer(), nullable=True),
    sa.Column('lng', sa.Integer(), nullable=True),
    sa.Column('deltaCases', sa.Integer(), nullable=True),
    sa.Column('deltaDeaths', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('report')
    # ### end Alembic commands ###
