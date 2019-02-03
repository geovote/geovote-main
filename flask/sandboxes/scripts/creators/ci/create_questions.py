from models.manager import Manager
from tests.utils import create_question
from utils.logger import logger

from utils.config import COMMAND_NAME, EMAIL_HOST

def create_questions():
    logger.info('create_questions')

    questions_by_name = {}

    text = 'Doit-on manger du quinoa pour sauver le monde ?'
    questions_by_name[text] = create_question(
        text=text
    )

    Manager.check_and_save(*questions_by_name.values())

    logger.info('created {} questions'.format(len(questions_by_name)))

    return questions_by_name
