"""empty message

Revision ID: 1cfa7506376b
Revises: 1244708a9a85
Create Date: 2014-08-14 05:06:12.492274

"""

# revision identifiers, used by Alembic.
revision = '1cfa7506376b'
down_revision = '1244708a9a85'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts', 'author_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('posts', 'author_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    ### end Alembic commands ###
