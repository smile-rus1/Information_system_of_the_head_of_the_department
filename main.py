import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from widjets.main_menu import Ui_MainWindow

from modules_for_forms.form_main_student import FormMainStudent
from modules_for_forms.form_main_group import FormMainGroup
from modules_for_forms.form_main_curators import FormMainCurators

from db_create import create_database


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_open_window_student.clicked.connect(lambda: FormMainStudent().show())
        self.ui.btn_open_window_group.clicked.connect(lambda: FormMainGroup().show())
        self.ui.btn_open_window_curator.clicked.connect(lambda: FormMainCurators().show())
        self.ui.btn_create_db.clicked.connect(lambda: create_database())


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(main_window)
    widget.setFixedHeight(255)
    widget.setFixedWidth(640)
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
