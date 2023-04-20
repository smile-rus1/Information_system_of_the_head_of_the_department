from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from models.data_base import Base


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    student_id = relationship("Student", backref=backref('groups'))
    curator_id = relationship("Curator", backref=backref('groups'))

    # def __repr__(self):
    #     info_group = f"{self.group_name}"
    #
    #     return info_group
