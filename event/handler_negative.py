from PyQt5.QtWidgets import QMessageBox


def handler_negative(message):
    mb1 = QMessageBox()
    mb1.setWindowTitle('Ошибка')
    mb1.setText(f'Произошла ошибка {message}')
    mb1.setIcon(QMessageBox.Warning)
    mb1.setStandardButtons(QMessageBox.Ok)
    mb1.exec_()
