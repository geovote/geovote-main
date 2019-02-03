""" ci """
from sandboxes.scripts.creators.ci.create_answers import *
from sandboxes.scripts.creators.ci.create_questions import *
from utils.logger import logger

def create_sandbox():
    logger.info('create_ci_sandbox...')
    create_questions()
    create_answers()
    logger.info('create_ci_sandbox...Done.')
