""" interact """
import os
from flask import Flask

from models.utils.db import db

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET', '+%+3Q23!zbc+!Dd@')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('POSTGRES_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
db.app = app

with app.app_context():
    from models.utils.install_models import install_models
    install_models()

# IMPORT A LOT OF TOOLS TO MAKE THEM AVAILABLE
# IN THE PYTHON SHELL
from models.manager import *
from models import *
from repository import *
from sandboxes import *
from sqlalchemy import *
