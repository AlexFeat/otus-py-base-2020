"""inset menu

Revision ID: ab35a242ce24
Revises: b32626f8837e
Create Date: 2021-04-11 15:57:21.875798

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Numeric


# revision identifiers, used by Alembic.
revision = 'ab35a242ce24'
down_revision = 'b32626f8837e'
branch_labels = None
depends_on = None

menu_table = table('menu',
    column('id', Integer),
    column('name', String),
    column('cost', Numeric)
)

def upgrade():
    op.bulk_insert(menu_table,
        [
            {'id': 1, 'name': 'Чай', 'cost': 0},
            {'id': 2, 'name': 'Кофе', 'cost': 0},
            {'id': 3, 'name': 'Борщ', 'cost': 0},
            {'id': 4, 'name': 'Окрошка', 'cost': 0},
            {'id': 5, 'name': 'Пюре', 'cost': 0},
            {'id': 6, 'name': 'Гречка', 'cost': 0},
            {'id': 7, 'name': 'Макароны', 'cost': 0},
            {'id': 8, 'name': 'Гуляш', 'cost': 0},
            {'id': 9, 'name': 'Котлеты куриные', 'cost': 0},
            {'id': 10, 'name': 'Скинная отбивная', 'cost': 0},
            {'id': 11, 'name': 'Эклер', 'cost': 0},
            {'id': 12, 'name': 'Пироженное катошка', 'cost': 0},
        ],
        multiinsert=True
    )


def downgrade():
    op.execute('DELETE FROM menu WHERE id <= 12;')
