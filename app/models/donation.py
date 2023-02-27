from sqlalchemy import Column, ForeignKey, Integer, Text

from app.core.db import Base
from app.models.mixins import CommonFieldsMixin


class Donation(CommonFieldsMixin, Base):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)
