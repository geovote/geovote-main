"""schema init

Revision ID: 75a5ca628a2e
Revises:
Create Date: 2019-01-05 22:31:58.467062

"""
from pathlib import Path
import os
from alembic import op


# revision identifiers, used by Alembic.
revision = '75a5ca628a2e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    sql_file_path = Path(os.path.dirname(os.path.realpath(__file__))) / 'schema_init.sql'

    with open(sql_file_path, 'r') as sql_file:
        data = sql_file.read()
    op.execute(data)


def downgrade():
    pass
