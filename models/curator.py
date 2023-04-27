from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from models.data_base import Base


class Curator(Base):
    __tablename__ = 'curators'
    id = Column(Integer, primary_key=True)
    name = Column(String)
