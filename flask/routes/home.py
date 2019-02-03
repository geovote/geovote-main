from flask import current_app as app, \
                  Blueprint,\
                  redirect,\
                  render_template,\
                  request

from utils.config import API_URL, GIT_TAG

blueprint = Blueprint(
    'home',
    __name__
)

app.register_blueprint(blueprint)

@app.route('/')
def render_home():
  return render_template('home.jinja', GIT_TAG=GIT_TAG)

@app.route('/', methods=['POST'])
def redirect_vote():
    question_id = request.form.get('questionId')
    vote_url = "{}/vote/{}".format(API_URL, question_id)
    return redirect(vote_url, code=302)
