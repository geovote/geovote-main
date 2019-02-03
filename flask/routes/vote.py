from flask import current_app as app,\
                  Blueprint,\
                  redirect,\
                  render_template,\
                  request

from models.answer import Answer
from models.manager import Manager
from models.question import Question
from utils.config import API_URL, APP_NAME, ENV, GIT_TAG
from utils.geolocation import distance_in_meters
from utils.human_ids import dehumanize
from utils.seal import get_footprint_from_request,\
                       get_sealprint_from_footprint,\
                       get_seal_from_sealprint

LOCAL_STORAGE_KEY = '{}-{}'.format(APP_NAME, ENV) if ENV != 'production' else APP_NAME

blueprint = Blueprint(
    'vote',
    __name__
)

app.register_blueprint(blueprint)

@app.route('/vote/<question_id>')
def render_vote(question_id):

    question = Question.query.filter_by(id=dehumanize(question_id))\
                             .first()

    if question is None:
        return render_template('error.jinja')

    footprint = get_footprint_from_request(request)
    has_voted = question.hasVoted(footprint)

    return render_template(
        'vote.jinja',
        footprint=footprint,
        GIT_TAG=GIT_TAG,
        has_voted=has_voted,
        LOCAL_STORAGE_KEY=LOCAL_STORAGE_KEY,
        question=question
    )

@app.route('/vote/<question_id>/form', methods=['POST'])
def post_vote(question_id):

    question = Question.query.filter_by(id=dehumanize(question_id))\
                             .first()
    if question is None:
        return render_template('error.jinja')

    if question.radius:
        vote_distance = distance_in_meters(
            float(question.latitude), float(question.longitude),
            float(request.form.get('latitude')), float(request.form.get('longitude'))
        )
        if vote_distance > question.radius:
            return render_template(
                'vote.jinja',
                GIT_TAG=GIT_TAG,
                has_voted=False,
                is_too_far=True,
                LOCAL_STORAGE_KEY=LOCAL_STORAGE_KEY,
                question=question
            )

    footprint = get_footprint_from_request(request)
    has_voted = question.hasVoted(footprint)
    if has_voted:
        return render_template(
            'error.jinja',
            GIT_TAG=GIT_TAG,
            LOCAL_STORAGE_KEY=LOCAL_STORAGE_KEY,
            message="Votre signature existe déjà pour ce vote."
        )

    footprint = get_sealprint_from_footprint(footprint)
    seal = get_seal_from_sealprint(footprint)
    voted_answers = []
    for (key, value) in request.form.items():
        if key.startswith('answer-'):

            answer = Answer.query.filter_by(id=dehumanize(value))\
                                 .first()
            if answer is None:
                return render_template('error.jinja')

            answer.addSeal(seal)
            voted_answers.append(answer)

    if voted_answers:
        Manager.check_and_save(*voted_answers)

    vote_url = "{}/vote/{}?footprint={}".format(API_URL, question_id, footprint)
    return redirect(vote_url, code=302)
