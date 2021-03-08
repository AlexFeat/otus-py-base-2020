"""added fields

Revision ID: 168dda8e7f42
Revises: adce97b1aebf
Create Date: 2021-03-07 15:56:23.040803

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '168dda8e7f42'
down_revision = 'adce97b1aebf'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'items',
        sa.Column(
            'ts_modify',
            sa.DateTime,
            server_default=sa.func.now(),
        ),
        schema='user',
    )
    op.add_column(
        'items',
        sa.Column(
            'ts_modify',
            sa.DateTime,
            server_default=sa.func.now(),
        ),
        schema='post',
    )


def downgrade():
    op.drop_column('items', 'ts_modify', schema='post')
    op.drop_column('items', 'ts_modify', schema='user')
