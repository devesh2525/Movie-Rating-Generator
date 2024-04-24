"""Add movie_title to Review model

Revision ID: 6420cc00f7fc
Revises: 02b8c920ba54
Create Date: 2024-04-15 01:44:46.406481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6420cc00f7fc'
down_revision = '02b8c920ba54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
