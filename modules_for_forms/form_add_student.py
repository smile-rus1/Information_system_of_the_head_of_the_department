from PyQt5.QtWidgets import QDialog, QMainWindow, QTableWidgetItem, QInputDialog, QLineEdit
from sqlalchemy import and_

from widjets.main_student_window import Ui_main_student_window
from widjets.form_add_student import Ui_FormAddStudent

from models.student import Student
from models.group import Group
from models.curator import Curator
from models.data_base import Session
from event.handler_negative import handler_negative
from event.handler_possitive import handler_successful


class FormAddStudent(QMainWindow, QDialog):
    def __init__(self, parent=None):
        super(FormAddStudent, self).__init__(parent)

        self.ui_form_add = Ui_FormAddStudent()
        self.ui_form_add.setupUi(self)

        self.setFixedHeight(525)
        self.setFixedWidth(265)

        self.load_group()

        self.ui_form_add.btn_add_student.clicked.connect(lambda: self.add_student())

    def load_group(self):
        session = Session()
        group = session.query(Group.name).all()
        lst_group = [self.tr(str(txt[0])) for txt in group]
        self.ui_form_add.cb_group_student.addItems(lst_group)
        session.close()

    def add_student(self):
        session = Session()
        try:
            if self.ui_form_add.edit_fio.text() == "":
                handler_negative("Поле ФИО не должно быть пустым!")
                return

            elif self.ui_form_add.edit_number_phone.text() == "":
                handler_negative("Поле Номер телефона не должно быть пустым!")
                return

            elif self.ui_form_add.edit_date_born.text() == "":
                handler_negative("Поле Дата рождения не должно быть пустым!")
                return

            elif self.ui_form_add.edit_form_education.text() == "":
                handler_negative("Поле Форма образование не должно быть пустым!")
                return

            elif self.ui_form_add.edit_place_residence.text() == "":
                handler_negative("Поле Место проживания не должно быть пустым!")
                return

            elif self.ui_form_add.edit_enrollement_order.text() == "":
                handler_negative("Поле Номер зачисления не должно быть пустым!")
                return

            group_student = session.query(Group.id).filter(Group.name.like(
                f"{self.ui_form_add.cb_group_student.currentText()}")).first()

            student = Student(FIO=self.ui_form_add.edit_fio.text(),
                              number_telephone=int(self.ui_form_add.edit_number_phone.text()),
                              date_born=self.ui_form_add.edit_date_born.text(),
                              place_of_residence=self.ui_form_add.edit_place_residence.text(),
                              enrollment_order=int(self.ui_form_add.edit_enrollement_order.text()),
                              form_of_education=self.ui_form_add.edit_form_education.text(),
                              group=group_student[0])
            session.add(student)
            handler_successful(f"Был добавлен студент {student.FIO}")
            session.commit()

        except Exception as ex:
            handler_negative(f"Данные не правильно введены! {ex}")
            session.rollback()

        finally:
            session.close()
