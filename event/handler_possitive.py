from PyQt5.QtWidgets import QMessageBox


def handler_successful(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(f"{text}")
    msg.setWindowTitle("Успех")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()
