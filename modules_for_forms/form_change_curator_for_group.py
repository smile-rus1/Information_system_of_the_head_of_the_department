from PyQt5.QtWidgets import QMainWindow, QDialog
from sqlalchemy import and_

from widjets.form_change_curator_for_group import Ui_FormChangeCurator

from models.student import Student
from models.group import Group
from models.curator import Curator

from models.data_base import Session

from event.handler_negative import handler_negative
from event.handler_possitive import handler_successful
from event.handler_question import handler_question

session = Session()


class FormChangeCurator(QMainWindow, QDialog):
    def __init__(self, parent=None) -> None:
        super(FormChangeCurator, self).__init__(parent)

        self.ui_form_change = Ui_FormChangeCurator()
        self.ui_form_change.setupUi(self)

        self.setFixedHeight(230)
        self.setFixedWidth(300)

        global session

        self.load_curators()
        self.load_groups()

        self.ui_form_change.btn_add_group.clicked.connect(lambda: self.change_curator())

    def load_curators(self) -> None:
        curators = [self.tr(str(curator[0])) for curator in session.query(Curator.name).all()]
        self.ui_form_change.cb_change_curator_group.addItems(curators)

    def load_groups(self):
        lst_group = [self.tr(str(txt[0])) for txt in session.query(Group.name).all()]
        self.ui_form_change.cb_choice_group.addItems(lst_group)

    def change_curator(self) -> None:
        try:
            group = session.query(Group).filter_by(id=session.query(Group.id)\
                .filter(and_(Group.name.like(f"{self.ui_form_change.cb_choice_group.currentText()}")))
                                                   .first()[0]).first()

            group.curator_id = session.query(Curator.id)\
                .filter(Curator.name.like(f"{self.ui_form_change.cb_change_curator_group.currentText()}")).first()[0]

            if handler_question(
                    f"Вы действительно хотите изменить у группы {self.ui_form_change.cb_choice_group.currentText()} куратора?"):
                session.commit()

                handler_successful(f"Был обновлен куратор у {self.ui_form_change.cb_choice_group.currentText()}")

            else:
                session.rollback()
                handler_negative("Данные не были добавлены!")

        except Exception as ex:
            session.rollback()
            handler_negative(ex)

        finally:
            session.close()
