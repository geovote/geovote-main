from flask import current_app as app,\
                  Blueprint,\
                  redirect,\
                  render_template,\
                  request

from models.manager import Manager
from models.question import Question
from repository.answers import create_answers_with_form_and_question
from utils.config import GIT_TAG, API_URL
from utils.human_ids import dehumanize, humanize

blueprint = Blueprint(
    'creation',
    __name__
)

app.register_blueprint(blueprint)

@app.route('/creation')
def render_creation():
  return render_template('creation.jinja', GIT_TAG=GIT_TAG)

@app.route('/creation/form', methods=['POST'])
def create_question_and_answers():
    question = Question()

    question.populateFromDict(request.form)

    answers = create_answers_with_form_and_question(request.form, question)

    Manager.check_and_save(question, *answers)

    vote_url = "{}/vote/{}".format(API_URL, humanize(question.id))
    return redirect(vote_url, code=302)
