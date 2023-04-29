from PyQt5.QtWidgets import QMainWindow, QDialog
from sqlalchemy import and_

from widjets.form_change_group_for_curator import Ui_FormChangeGroup

from models.student import Student
from models.group import Group
from models.curator import Curator

from models.data_base import Session

from event.handler_negative import handler_negative
from event.handler_possitive import handler_successful
from event.handler_question import handler_question

session = Session()


class FormChangeGroup(QMainWindow, QDialog):
    def __init__(self, parent=None) -> None:
        super(FormChangeGroup, self).__init__(parent)
        self.ui_change_group = Ui_FormChangeGroup()
        self.ui_change_group.setupUi(self)

        self.setFixedHeight(250)
        self.setFixedWidth(270)

        global session

        self.load_curators()
        self.load_groups()
        self.ui_change_group.btn_add_change.clicked.connect(lambda: self.change_group())

    def load_curators(self) -> None:
        curators = [self.tr(str(curator[0])) for curator in session.query(Curator.name).all()]
        self.ui_change_group.cb_choice_curator.addItems(curators)

    def load_groups(self):
        lst_group = [self.tr(str(txt[0])) for txt in session.query(Group.name).all()]
        self.ui_change_group.cb_change_group.addItems(lst_group)

    def change_group(self) -> None:
        try:
            group = session.query(Group).filter_by(id=session.query(Group.id)\
                .filter(and_(Group.name.like(f"{self.ui_change_group.cb_change_group.currentText()}")))
                                                   .first()[0]).first()

            group.curator_id = session.query(Curator.id)\
                .filter(Curator.name.like(f"{self.ui_change_group.cb_choice_curator.currentText()}")).first()[0]

            if handler_question(
                    f"Вы действительно хотите изменить у куратора {self.ui_change_group.cb_choice_curator.currentText()} группу?"):
                session.commit()

                handler_successful(f"Был обновлена группа у {self.ui_change_group.cb_choice_curator.currentText()}")

            else:
                session.rollback()
                handler_negative("Данные не были добавлены!")

        except Exception as ex:
            session.rollback()
            handler_negative(ex)

        finally:
            session.close()
