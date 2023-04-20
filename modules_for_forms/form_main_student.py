from PyQt5.QtWidgets import QDialog, QMainWindow, QTableWidgetItem

from widjets.main_student_window import Ui_main_student_window

from models.student import Student
from models.group import Group
from models.curator import Curator
from models.data_base import Session
from event.handler_negative import handler_negative


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

        self.ui_student.btn_out_all_student.clicked.connect(lambda: self.show_all_info_student())

    def show_all_info_student(self):
        self.ui_student.table_all_student.setRowCount(9999)

        session = Session()
        try:
            lst_all_info_student = [ls for ls in session.query(Student.id, Student.FIO, Student.number_telephone,
                                                               Student.date_born, Student.place_of_residence,
                                                               Student.form_of_education, Group.name,
                                                               Student.enrollment_order)
                                                                .join(Group, Group.id == Student.group)]

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
            handler_negative(ex)

        finally:
            session.close()
