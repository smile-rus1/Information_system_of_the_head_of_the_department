from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMainWindow, QTableWidgetItem, QInputDialog, QLineEdit
from sqlalchemy import and_

from widjets.main_student_window import Ui_main_student_window
from modules_for_forms.form_add_student import FormAddStudent

from models.student import Student
from models.group import Group
from models.curator import Curator
from models.data_base import Session
from event.handler_negative import handler_negative
from event.handler_possitive import handler_successful
from event.handler_question import handler_question


class FormMainStudent(QMainWindow, QDialog):
    def __init__(self, parent=None):
        super(FormMainStudent, self).__init__(parent)

        self.ui_student = Ui_main_student_window()
        self.ui_student.setupUi(self)

        self.setFixedHeight(435)
        self.setFixedWidth(1105)

        self.ui_student.table_all_student.setColumnWidth(0, 10)
        self.ui_student.table_all_student.setColumnWidth(1, 100)
        self.ui_student.table_all_student.setColumnWidth(2, 100)
        self.ui_student.table_all_student.setColumnWidth(3, 100)
        self.ui_student.table_all_student.setColumnWidth(4, 150)
        self.ui_student.table_all_student.setColumnWidth(5, 100)
        self.ui_student.table_all_student.setColumnWidth(6, 100)
        self.ui_student.table_all_student.setColumnWidth(7, 150)

        self.ui_student.cb_choice_filter.currentIndexChanged.connect(self.check_combo)

        self.ui_student.btn_out_all_student.clicked.connect(lambda: self.show_all_info_student())
        self.ui_student.btn_show_filter_data.clicked.connect(lambda: self.show_filter_info())
        self.ui_student.btn_open_delete_student_form.clicked.connect(lambda: self.delete_student())
        self.ui_student.btn_open_add_student_form.clicked.connect(lambda: self.show_form_add_student())
        self.ui_student.btn_save_change.clicked.connect(lambda: self.update_student())

    def find_filter_info(self, filter_text: str, operation: str):
        session = Session()
        if operation == "id":
            filter_operation = Student.id

        if operation == "ФИО":
            filter_operation = Student.FIO

        if operation == "Номер телефона":
            filter_operation = Student.number_telephone

        if operation == "Дата рождения":
            filter_operation = Student.date_born

        if operation == "Способ обучения":
            filter_operation = Student.form_of_education

        if operation == "Группа":
            info = session.query(Student.id, Student.FIO, Student.number_telephone, Student.date_born,
                                 Student.place_of_residence, Student.form_of_education, Group.name,
                                 Student.enrollment_order).join(Group).filter(Student.group == Group.id). \
                filter(and_(Group.name.like(f"%{filter_text}%")))
            return info

        try:
            info_like = session.query(Student.id, Student.FIO, Student.number_telephone,
                                      Student.date_born, Student.place_of_residence,
                                      Student.form_of_education, Group.name,
                                      Student.enrollment_order) \
                .join(Group, Group.id == Student.group).filter(and_(filter_operation.like(f"%{filter_text}%")))

            return info_like

        except Exception as ex:
            handler_negative(ex)

        finally:
            session.close()

    def check_combo(self):
        if self.ui_student.cb_choice_filter.currentText() != "":
            self.ui_student.edit_filter.setEnabled(True)
            self.ui_student.edit_filter.setPlaceholderText("Введите данные")
        else:
            self.ui_student.edit_filter.setEnabled(False)

    def show_filter_info(self):
        if self.ui_student.cb_choice_filter.currentText() == "":
            handler_negative("Вы не выбрали критерий выбора!")
            return

        if self.ui_student.edit_filter.text() == "":
            handler_negative("Вы не написали данные")
            return

        self.ui_student.table_all_student.setRowCount(0)

        text_filter = self.ui_student.edit_filter.text()
        operation = self.ui_student.cb_choice_filter.currentText()

        info = self.find_filter_info(text_filter, operation)
        self.ui_student.table_all_student.setRowCount(len(list(info)))
        for i, row in enumerate(info):
            tablerow = 0
            self.ui_student.table_all_student.setItem(i, 0, QTableWidgetItem(str(row[tablerow])))
            tablerow += 1
            self.ui_student.table_all_student.setItem(i, 1, QTableWidgetItem(str(row[tablerow])))
            tablerow += 1
            self.ui_student.table_all_student.setItem(i, 2, QTableWidgetItem(str(row[tablerow])))
            tablerow += 1
            self.ui_student.table_all_student.setItem(i, 3, QTableWidgetItem(str(row[tablerow])))
            tablerow += 1
            self.ui_student.table_all_student.setItem(i, 4, QTableWidgetItem(str(row[tablerow])))
            tablerow += 1
            self.ui_student.table_all_student.setItem(i, 5, QTableWidgetItem(str(row[tablerow])))
            tablerow += 1
            self.ui_student.table_all_student.setItem(i, 6, QTableWidgetItem(str(row[tablerow])))
            tablerow += 1
            self.ui_student.table_all_student.setItem(i, 7, QTableWidgetItem(str(row[tablerow])))

    def show_all_info_student(self):
        session = Session()
        try:
            lst_all_info_student = [ls for ls in session.query(Student.id, Student.FIO, Student.number_telephone,
                                                               Student.date_born, Student.place_of_residence,
                                                               Student.form_of_education, Group.name,
                                                               Student.enrollment_order)
            .join(Group, Group.id == Student.group)]
            self.ui_student.table_all_student.setRowCount(len(lst_all_info_student))

            for i, row in enumerate(lst_all_info_student):
                tablerow = 0
                self.ui_student.table_all_student.setItem(i, 0, QTableWidgetItem(str(row[tablerow])))
                tablerow += 1
                self.ui_student.table_all_student.setItem(i, 1, QTableWidgetItem(str(row[tablerow])))
                tablerow += 1
                self.ui_student.table_all_student.setItem(i, 2, QTableWidgetItem(str(row[tablerow])))
                tablerow += 1
                self.ui_student.table_all_student.setItem(i, 3, QTableWidgetItem(str(row[tablerow])))
                tablerow += 1
                self.ui_student.table_all_student.setItem(i, 4, QTableWidgetItem(str(row[tablerow])))
                tablerow += 1
                self.ui_student.table_all_student.setItem(i, 5, QTableWidgetItem(str(row[tablerow])))
                tablerow += 1
                self.ui_student.table_all_student.setItem(i, 6, QTableWidgetItem(str(row[tablerow])))
                tablerow += 1
                self.ui_student.table_all_student.setItem(i, 7, QTableWidgetItem(str(row[tablerow])))

        except Exception as ex:
            session.rollback()
            handler_negative(ex)

        finally:
            session.close()

    def delete_student(self):
        text, pressed = QInputDialog.getText(self, "Введите ФИО студента, которого хотите удалить", "Введите ФИО",
                                             QLineEdit.Normal)
        if text == "":
            handler_negative("Вы не ввели данные!")

        if pressed and text != "":
            session = Session()
            try:
                id_student = session.query(Student.id).filter(Student.FIO.like(f"%{text}%")).first()[0]
                student = session.query(Student).filter_by(id=id_student).first()

                session.delete(student)
                session.commit()
                handler_successful(f"Был удален {student.FIO}")

            except:
                session.rollback()
                handler_negative("Не правильно ввели данные")

            finally:
                session.close()

    def show_form_add_student(self):
        self.UI_form_add_sudent = FormAddStudent(parent=self)
        self.UI_form_add_sudent.show()

    def update_student(self): # тут какой-то баг хз
        session = Session()
        try:
            data_student = []

            for row in range(self.ui_student.table_all_student.rowCount()):
                rowdata = []
                for col in range(self.ui_student.table_all_student.columnCount()):
                    rowdata.append(self.ui_student.table_all_student.item(row, col).data(Qt.EditRole))
                data_student.append(tuple(rowdata))

            for i, dt in enumerate(data_student):
                st = 0
                data = []
                data.append(dt[st])
                st += 1
                data.append(dt[st])
                st += 1
                data.append(dt[st])
                st += 1
                data.append(dt[st])
                st += 1
                data.append(dt[st])
                st += 1
                data.append(dt[st])
                st += 1
                data.append(dt[st])
                st += 1
                data.append(dt[st])

                student = session.query(Student).filter_by(id=int(data[0])).first()
                student.FIO = data[1]
                student.number_telephone = int(data[2])
                student.date_born = data[3]
                student.place_of_residence = data[4]
                student.form_of_education = data[5]
                student.group = session.query(Group.id).filter(and_(Group.name.like(f"%{data[6]}%"))).scalar_subquery()
                student.enrollment_order = data[7]

            if handler_question("Вы действительно хотите сохранить?"):
                handler_successful("Данные успено сохранены!")
                session.commit()


            else:
                handler_successful("Данные не были сохранены!")
                session.rollback()

        except Exception as ex:
            session.rollback()
            handler_negative(ex)

        finally:
            session.close()
