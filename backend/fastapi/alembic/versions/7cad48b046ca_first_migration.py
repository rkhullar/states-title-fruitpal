"""first migration

Revision ID: 7cad48b046ca
Revises: 
Create Date: 2022-02-17 21:34:05.017637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7cad48b046ca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vendors',
    sa.Column('country', sa.String(), nullable=False),
    sa.Column('commodity', sa.String(), nullable=False),
    sa.Column('variable_overhead', sa.Numeric(), nullable=False),
    sa.PrimaryKeyConstraint('country', 'commodity')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vendors')
    # ### end Alembic commands ###
