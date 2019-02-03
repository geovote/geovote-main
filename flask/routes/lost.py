from flask import current_app as app, \
                  Blueprint,\
                  render_template

from utils.config import GIT_TAG

blueprint = Blueprint(
    'lost',
    __name__
)

app.register_blueprint(blueprint)

@app.route('/<lost>')
def render_lost(lost):
  return render_template('error.jinja', GIT_TAG=GIT_TAG)
