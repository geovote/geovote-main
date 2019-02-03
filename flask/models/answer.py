from sqlalchemy import BigInteger,\
                       Binary,\
                       Column,\
                       ForeignKey,\
                       String,\
                       Text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.event import listens_for
from sqlalchemy.orm import relationship

from models.utils.db import Model
from models.manager import Manager
from utils.seal import is_footprint_from_seal

class Answer(Manager, Model):

    finalCount = Column(BigInteger)

    seals = Column(ARRAY(Binary(60)))

    text = Column(Text)

    questionId = Column(BigInteger,
                        ForeignKey('question.id'),
                        nullable=False,
                        index=True)

    question = relationship('Question',
                            foreign_keys=[questionId],
                            backref='answers')

    @property
    def count(self):
        if self.seals:
            return len(self.seals)
        return 0

    def addSeal(self, seal):
        if self.seals:
            self.seals = self.seals + [seal]
        else:
            self.seals = [seal]

    def cleanAfterVote(self):
        self.finalCount = self.count
        self.seals = []

    def hasVoted(self, footprint):
        if not self.seals:
            return False
        for seal in self.seals:
            if is_footprint_from_seal(footprint, seal):
                return True
