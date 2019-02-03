from datetime import datetime, timedelta
import subprocess
from sqlalchemy import BigInteger,\
                       Boolean,\
                       Column,\
                       DateTime,\
                       Numeric,\
                       Text
from sqlalchemy.event import listens_for

from models.utils.db import db, Model
from models.manager import Manager
from utils.config import FLASK_ROOT_PATH

class Question(Manager, Model):
    isPublic = Column(Boolean)

    isPublished = Column(Boolean, nullable=False, default=False)

    latitude = Column(Numeric(8, 5), nullable=True)

    longitude = Column(Numeric(8, 5), nullable=True)

    publishDuration = Column(BigInteger, nullable=False, default=180)

    radius = Column(BigInteger)

    text = Column(Text)

    voteDate = Column(DateTime,
                      nullable=False,
                      default=datetime.utcnow)

    voteDuration = Column(BigInteger, nullable=False, default=180)

    @property
    def publishDate(self):
        return self.voteDate + timedelta(seconds=self.voteDuration)

    def secondsLeftBeforePublish(self):
        timedeltaBeforePublish = self.publishDate - datetime.utcnow()
        return timedeltaBeforePublish.total_seconds()

    def timeLeftBeforePublish(self):
        secondsLeftBeforePublish = self.secondsLeftBeforePublish()
        m, s = divmod(secondsLeftBeforePublish, 60)
        return "%02d:%02d" % (m, s)

    def secondsLeftAfterPublish(self):
        timedeltaAfterPublish = self.publishDate \
                                + timedelta(seconds=self.publishDuration) \
                                - datetime.utcnow()
        return timedeltaAfterPublish.total_seconds()

    def timeLeftAfterPublish(self):
        secondsLeftAfterPublish = self.secondsLeftAfterPublish()
        m, s = divmod(secondsLeftAfterPublish, 60)
        return "%02d:%02d" % (m, s)

    def hasVoted(self, footprint):
        for answer in self.answers:
            if answer.hasVoted(footprint):
                return True
        return False

    def cleanAfterVote(self):
        for answer in self.answers:
            answer.cleanAfterVote()

    def cleanAfterPublish(self):
        if self.isPublic:
            return
        for answer in self.answers:
            db.session.delete(answer)
        db.session.delete(self)
        db.session.commit()

class MissingCoordsWithRadiusException(Exception):
    pass

def _check_coords_with_radius(question):
    if question.radius and (not question.latitude or not question.longitude):
        raise MissingCoordsWithRadiusException

@listens_for(Question, 'before_insert')
def after_insert(mapper, connect, self):
    _check_coords_with_radius(self)

def _trigger_vote(question):
    subprocess.Popen('PYTHONPATH="." python scripts/manager.py vote'
                     + ' --id ' + str(question.id),
                     shell=True,
                     cwd=FLASK_ROOT_PATH)

@listens_for(Question, 'after_insert')
def after_insert(mapper, connect, self):
    _trigger_vote(self)

def _trigger_publish(question):
    subprocess.Popen('PYTHONPATH="." python scripts/manager.py publish'
                     + ' --id ' + str(question.id),
                     shell=True,
                     cwd=FLASK_ROOT_PATH)

@listens_for(Question, 'after_update')
def after_update(mapper, connect, self):
    if self.isPublished:
        _trigger_publish(self)

class NotDeletablePublicQuestionException(Exception):
    pass

@listens_for(Question, 'before_delete')
def after_insert(mapper, connect, self):
    if self.isPublic:
        raise NotDeletablePublicQuestionException
