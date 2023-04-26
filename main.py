import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from widjets.main_menu import Ui_MainWindow

from modules_for_forms.form_main_student import FormMainStudent


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_open_window_student.clicked.connect(lambda: self.open_window_student())

    def open_window_student(self):
        self.UI_main_student = FormMainStudent(parent=self)
        self.UI_main_student.show()

    def open_window_groups(self):
        self.UI_main_group = ...


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
