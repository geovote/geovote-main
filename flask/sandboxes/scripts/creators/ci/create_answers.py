from models.manager import Manager
from models.question import Question
from tests.utils import create_answer
from utils.config import COMMAND_NAME, EMAIL_HOST
from utils.logger import logger
from utils.seal import get_seal_from_sealprint

def create_answers():
    logger.info('create_answers')

    answers_by_name = {}


    question_text = 'Doit-on manger du quinoa pour sauver le monde ?'
    question = Question.query.filter_by(text=question_text).one()



    answer_text = "Oui"
    seals = [get_seal_from_sealprint(ip) for ip in ["192.168.48.3", "192.167.38.1"]]
    answers_by_name['{} {}'.format(question_text, answer_text)] = create_answer(
        text=answer_text,
        question=question,
        seals=seals
    )
    answer_text = "Non"
    answers_by_name['{} {}'.format(question_text, answer_text)] = create_answer(
        text=answer_text,
        question=question
    )


    Manager.check_and_save(*answers_by_name.values())

    logger.info('created {} answers'.format(len(answers_by_name)))

    return answers_by_name
