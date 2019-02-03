from models.utils.db import db
from models import Answer,\
                   Question
from utils.logger import logger

def clean_all_database():
    """ Order of deletions matters because of foreign key constraints """
    logger.info("clean all the database...")
    Answer.query.delete()
    Question.query.delete()
    db.session.commit()
    logger.info("clean all the database...Done.")
