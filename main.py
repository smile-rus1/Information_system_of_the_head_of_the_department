import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from widjets.main_menu import Ui_MainWindow

from modules_for_forms.form_main_student import FormMainStudent
from modules_for_forms.form_main_group import FormMainGroup
from modules_for_forms.form_main_curators import FormMainCurators


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_open_window_student.clicked.connect(lambda: self.open_window_student())
        self.ui.btn_open_window_group.clicked.connect(lambda: self.open_window_groups())
        self.ui.btn_open_window_curator.clicked.connect(lambda: self.open_window_curators())

    def open_window_student(self):
        UI_main_student = FormMainStudent()
        UI_main_student.show()

    def open_window_groups(self):
        UI_main_group = FormMainGroup()
        UI_main_group.show()

    def open_window_curators(self):
        UI_main_curators = FormMainCurators()
        UI_main_curators.show()


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(main_window)
    widget.setFixedHeight(235)
    widget.setFixedWidth(640)
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
