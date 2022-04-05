"""criando tabela call_records

Revision ID: e105e6ad4def
Revises: 
Create Date: 2022-04-05 10:07:08.344352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e105e6ad4def'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('call_records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('source', sa.String(), nullable=False),
    sa.Column('destination', sa.String(), nullable=False),
    sa.Column('start_time', sa.Date(), nullable=True),
    sa.Column('end_time', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('call_records')
    # ### end Alembic commands ###
