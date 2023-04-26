from PyQt5.QtWidgets import QMessageBox


def handler_question(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(f"{text}")
    msg.setWindowTitle("Вопрос")
    msg.yes = msg.addButton("Да", QMessageBox.AcceptRole)
    msg.no = msg.addButton("Нет", QMessageBox.RejectRole)
    msg.exec_()

    if msg.clickedButton() == msg.yes:
        return True

    return False
