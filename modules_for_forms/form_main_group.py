from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMainWindow, QTableWidgetItem, QInputDialog, QLineEdit

from models.data_base import Session
from models.group import Group
from models.curator import Curator
from models.student import Student
from sqlalchemy import and_, func
from sqlalchemy.orm import joinedload

from widjets.main_group_window import Ui_main_group_window

session = Session()


class FormMainGroup(QMainWindow, QDialog):
    global session

    def __init__(self, parent=None):
        super(FormMainGroup, self).__init__(parent)
        self.ui_groups = Ui_main_group_window()
        self.ui_groups.setupUi(self)

        self.setFixedHeight(425)
        self.setFixedWidth(785)

        self.ui_groups.table_all_groups.setColumnWidth(0, 10)
        self.ui_groups.table_all_groups.setColumnWidth(1, 100)
        self.ui_groups.table_all_groups.setColumnWidth(2, 100)
        self.ui_groups.table_all_groups.setColumnWidth(3, 150)

        self.ui_groups.cb_choice_filter.currentIndexChanged.connect(self.check_combo)
        self.ui_groups.btn_out_all_groups.clicked.connect(lambda: self.show_all_info_group())

    def check_combo(self):
        if self.ui_groups.cb_choice_filter.currentText() != "":
            self.ui_groups.edit_filter.setEnabled(True)
            self.ui_groups.edit_filter.setPlaceholderText("Введите данные")
        else:
            self.ui_groups.edit_filter.setEnabled(False)

    def show_all_info_group(self):
        try:
            lst_info = [info for info in session.query(Group.id, Group.name, Curator.name,
                func.ifnull(func.count(Student.group), 0))
                    .join(Curator, Curator.id == Group.curator_id)
                    .outerjoin(Student, Student.group == Group.id)
                    .group_by(Group.name, Curator.name)
                        ]

            self.ui_groups.table_all_groups.setRowCount(len(lst_info))

            for i, row in enumerate(lst_info):
                tablerow = 0
                self.ui_groups.table_all_groups.setItem(i, 0, QTableWidgetItem(str(row[tablerow])))
                tablerow += 1
                self.ui_groups.table_all_groups.setItem(i, 1, QTableWidgetItem(str(row[tablerow])))
                tablerow += 1
                self.ui_groups.table_all_groups.setItem(i, 2, QTableWidgetItem(str(row[tablerow])))
                tablerow += 1
                self.ui_groups.table_all_groups.setItem(i, 3, QTableWidgetItem(str(row[tablerow])))

        finally:
            session.close()
