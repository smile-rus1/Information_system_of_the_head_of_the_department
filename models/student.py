from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey

from models.data_base import Base


class Student(Base):
    __tablename__ = "student"

    id = Column(INTEGER, primary_key=True)
    FIO = Column(VARCHAR(100), nullable=False)
    number_telephone = Column(INTEGER, nullable=False, unique=True)
    date_born = Column(VARCHAR(30), nullable=False)
    place_of_residence = Column(VARCHAR(150), nullable=False)
    enrollment_order = Column(INTEGER, unique=True)
    form_of_education = Column(VARCHAR(30), nullable=False)

    group = Column(INTEGER, ForeignKey("groups.id", ondelete="SET NULL"))

    def __repr__(self):
        info = f"{self.id} {self.FIO} {self.number_telephone} " \
               f"{self.date_born} {self.place_of_residence} " \
               f"{self.enrollment_order} {self.form_of_education} " \
               f"{self.group}"

        return info
