from psycopg2 import STRING
from psycopg2.extensions import register_type, new_array_type

from models.utils.db import db, Model


def install_models():
    db.create_all()
    db.session.commit()
