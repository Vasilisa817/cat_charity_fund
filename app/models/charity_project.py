from sqlalchemy import Column, String, Text

from app.core.config import settings
from app.core.db import Base
from app.models.mixins import CommonFieldsMixin


class CharityProject(CommonFieldsMixin, Base):
    name = Column(String(settings.str_length), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self) -> str:
        return f'Фонд {self.name}'
