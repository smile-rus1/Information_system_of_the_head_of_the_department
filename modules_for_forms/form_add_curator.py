from PyQt5.QtWidgets import QMainWindow, QDialog

from widjets.form_add_curator import Ui_FormAddCurator

from models.student import Student
from models.group import Group
from models.curator import Curator

from models.data_base import Session

from event.handler_negative import handler_negative
from event.handler_possitive import handler_successful
from event.handler_question import handler_question

session = Session()


class FormAddCurator(QMainWindow, QDialog):
    def __init__(self, parent=None) -> None:
        super(FormAddCurator, self).__init__(parent)

        self.ui_curator_add = Ui_FormAddCurator()
        self.ui_curator_add.setupUi(self)
        global session

        self.setFixedHeight(140)
        self.setFixedWidth(275)

        self.ui_curator_add.btn_add_curator.clicked.connect(lambda: self.add_curator())

    def add_curator(self) -> None:
        try:
            if self.ui_curator_add.edit_name_curator.text() == "":
                handler_negative("Поле 'Название группы' не долно быть пустым!")
                return

            curator = Curator(name=self.ui_curator_add.edit_name_curator.text())
            session.add(curator)

            if handler_question(
                    f"Вы действительно хотите добавить группу {self.ui_curator_add.edit_name_curator.text()}?"):
                session.commit()
                handler_successful(f"Была добавлена группа {self.ui_curator_add.edit_name_curator.text()}")

            else:
                session.rollback()
                handler_successful("Данные не были добавлены!")

        except Exception as ex:
            session.rollback()
            handler_negative(ex)

        finally:
            session.close()
