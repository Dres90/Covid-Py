"""empty message

Revision ID: dcc3e44b4f24
Revises: c065a4328066
Create Date: 2020-03-25 15:49:29.072803

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcc3e44b4f24'
down_revision = 'c065a4328066'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('date',
    sa.Column('id', sa.String(length=2), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_date_timestamp'), 'date', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_date_timestamp'), table_name='date')
    op.drop_table('date')
    # ### end Alembic commands ###