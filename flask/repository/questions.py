from time import sleep

from models.manager import Manager
from models.question import Question

def trigger_vote(question_id):
    question = Question.query.get(question_id)

    sleep(question.voteDuration)

    question.cleanAfterVote()

    question.isPublished = True

    Manager.check_and_save(question, *question.answers)

def trigger_publish(question_id):
    question = Question.query.get(question_id)

    # no need to do something if we can keep data public
    if question.isPublic:
        return

    sleep(question.publishDuration)

    question.cleanAfterPublish()
