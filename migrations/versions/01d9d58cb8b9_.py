"""empty message

Revision ID: 01d9d58cb8b9
Revises: ef8c883c00f4
Create Date: 2020-11-22 14:08:52.903058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01d9d58cb8b9'
down_revision = 'ef8c883c00f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('artist_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'shows', 'artists', ['artist_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'shows', type_='foreignkey')
    op.drop_column('shows', 'artist_id')
    # ### end Alembic commands ###
