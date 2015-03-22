"""empty message

Revision ID: 10da9a5f6d98
Revises: None
Create Date: 2015-03-21 12:38:38.518711

"""

# revision identifiers, used by Alembic.
revision = '10da9a5f6d98'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('author_id', sa.Integer(), nullable=True))
    op.alter_column('posts', 'description',
               existing_type=sa.VARCHAR(length=100000),
               nullable=False)
    op.alter_column('posts', 'title',
               existing_type=sa.VARCHAR(length=10000),
               nullable=False)
    op.create_foreign_key(None, 'posts', 'users', ['author_id'], ['id'])
    op.add_column('users', sa.Column('name', sa.String(), nullable=False))
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.drop_column('users', 'name')
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.alter_column('posts', 'title',
               existing_type=sa.VARCHAR(length=10000),
               nullable=True)
    op.alter_column('posts', 'description',
               existing_type=sa.VARCHAR(length=100000),
               nullable=True)
    op.drop_column('posts', 'author_id')
    ### end Alembic commands ###
