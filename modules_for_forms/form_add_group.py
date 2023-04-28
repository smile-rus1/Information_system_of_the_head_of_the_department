from PyQt5.QtWidgets import QMainWindow, QDialog

from widjets.form_add_group import Ui_FormAddGroup

from models.student import Student
from models.group import Group
from models.curator import Curator

from models.data_base import Session

from event.handler_negative import handler_negative
from event.handler_possitive import handler_successful
from event.handler_question import handler_question

session = Session()


class FormAddGroup(QMainWindow, QDialog):
    def __init__(self, parent=None) -> None:
        super(FormAddGroup, self).__init__(parent)

        self.ui_group_add = Ui_FormAddGroup()
        self.ui_group_add.setupUi(self)
        global session

        self.setFixedHeight(220)
        self.setFixedWidth(285)

        self.load_curator()
        self.ui_group_add.btn_add_group.clicked.connect(lambda: self.add_group())

    def load_curator(self) -> None:
        curators = [self.tr(str(curator[0])) for curator in session.query(Curator.name)\
            .outerjoin(Group, Curator.id == Group.curator_id) \
            .filter(Group.curator_id.is_(None)).distinct() \
            .all()]

        self.ui_group_add.cb_curator_group.addItems(curators)

    def add_group(self) -> None:
        try:
            if self.ui_group_add.edit_name_group.text() == "":
                handler_negative("Поле 'Название группы' не долно быть пустым!")
                return

            if self.ui_group_add.cb_curator_group.currentText() == "":
                handler_negative("Поле 'Куратор группы' не долно быть пустым!")
                return

            group = Group(name=self.ui_group_add.edit_name_group.text(),
                          curator_id=session.query(Curator.id) \
                          .filter(Curator.name.like(
                              f"{self.ui_group_add.cb_curator_group.currentText()}")).scalar_subquery())
            session.add(group)

            if handler_question(
                    f"Вы действительно хотите добавить группу {self.ui_group_add.cb_curator_group.currentText()}?"):
                session.commit()
                handler_successful(f"Была добавлена группа {self.ui_group_add.cb_curator_group.currentText()}")

            else:
                session.rollback()
                handler_successful("Данные не были добавлены!")

        except Exception as ex:
            session.rollback()
            handler_negative(ex)

        finally:
            session.close()
