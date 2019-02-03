from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

Model = db.Model

def get_model_with_table_name(table_name):
    for model in db.Model._decl_class_registry.values():
        if not hasattr(model, '__table__'):
            continue
        if model.__tablename__ == table_name:
            return model
