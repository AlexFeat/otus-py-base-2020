"""added tables : user and post

Revision ID: adce97b1aebf
Revises: a7ebe7a84955
Create Date: 2021-03-07 15:18:04.897689

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adce97b1aebf'
down_revision = 'a7ebe7a84955'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('CREATE SCHEMA "user"')
    op.create_table(
        'items',
        sa.Column('id', sa.BIGINT, primary_key=True),
        sa.Column('username', sa.VARCHAR(32), nullable=False),
        sa.Column('name', sa.VARCHAR(128)),
        sa.Column('email', sa.VARCHAR(128), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username'),
        schema='user'
    )
    op.execute('CREATE SCHEMA "post"')
    op.create_table(
        'items',
        sa.Column('id', sa.BIGINT, primary_key=True),
        sa.Column('user_id', sa.BIGINT, nullable=False),
        sa.Column('title', sa.VARCHAR(128), nullable=False),
        sa.Column('body', sa.Text),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['user_id'], ['user.items.id']),
        schema='post',
    )


def downgrade():
    op.drop_table('items', schema="post")
    op.execute('DROP SCHEMA "post"')
    op.drop_table('items', schema="user")
    op.execute('DROP SCHEMA "user"')
