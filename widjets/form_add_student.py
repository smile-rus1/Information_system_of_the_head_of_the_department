# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_add_student.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormAddStudent(object):
    def setupUi(self, FormAddStudent):
        FormAddStudent.setObjectName("FormAddStudent")
        FormAddStudent.resize(266, 523)
        FormAddStudent.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.centralwidget = QtWidgets.QWidget(FormAddStudent)
        self.centralwidget.setObjectName("centralwidget")
        self.edit_fio = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_fio.setEnabled(True)
        self.edit_fio.setGeometry(QtCore.QRect(10, 30, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.edit_fio.setFont(font)
        self.edit_fio.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edit_fio.setObjectName("edit_fio")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.edit_number_phone = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_number_phone.setEnabled(True)
        self.edit_number_phone.setGeometry(QtCore.QRect(10, 100, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.edit_number_phone.setFont(font)
        self.edit_number_phone.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edit_number_phone.setObjectName("edit_number_phone")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 75, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.edit_date_born = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_date_born.setEnabled(True)
        self.edit_date_born.setGeometry(QtCore.QRect(10, 170, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.edit_date_born.setFont(font)
        self.edit_date_born.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edit_date_born.setObjectName("edit_date_born")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 145, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 410, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.edit_form_education = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_form_education.setEnabled(True)
        self.edit_form_education.setGeometry(QtCore.QRect(10, 300, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.edit_form_education.setFont(font)
        self.edit_form_education.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edit_form_education.setObjectName("edit_form_education")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 275, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.edit_place_residence = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_place_residence.setEnabled(True)
        self.edit_place_residence.setGeometry(QtCore.QRect(10, 230, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.edit_place_residence.setFont(font)
        self.edit_place_residence.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edit_place_residence.setObjectName("edit_place_residence")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 210, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.cb_group_student = QtWidgets.QComboBox(self.centralwidget)
        self.cb_group_student.setGeometry(QtCore.QRect(10, 440, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cb_group_student.setFont(font)
        self.cb_group_student.setCurrentText("")
        self.cb_group_student.setObjectName("cb_group_student")
        self.btn_add_student = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_student.setGeometry(QtCore.QRect(10, 490, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add_student.setFont(font)
        self.btn_add_student.setStyleSheet("QPushButton {background-color: rgb(133, 125, 86); \n"
"color: White; border-radius: 10px;}\n"
"QPushButton:pressed {background-color:rgb(43, 252, 50) ; }")
        self.btn_add_student.setAutoDefault(False)
        self.btn_add_student.setDefault(False)
        self.btn_add_student.setFlat(False)
        self.btn_add_student.setObjectName("btn_add_student")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 345, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.edit_enrollement_order = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_enrollement_order.setEnabled(True)
        self.edit_enrollement_order.setGeometry(QtCore.QRect(10, 370, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.edit_enrollement_order.setFont(font)
        self.edit_enrollement_order.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edit_enrollement_order.setObjectName("edit_enrollement_order")
        FormAddStudent.setCentralWidget(self.centralwidget)

        self.retranslateUi(FormAddStudent)
        QtCore.QMetaObject.connectSlotsByName(FormAddStudent)

    def retranslateUi(self, FormAddStudent):
        _translate = QtCore.QCoreApplication.translate
        FormAddStudent.setWindowTitle(_translate("FormAddStudent", "Добавление студентов"))
        self.edit_fio.setPlaceholderText(_translate("FormAddStudent", "ФИО"))
        self.label.setText(_translate("FormAddStudent", "Введите ФИО"))
        self.edit_number_phone.setPlaceholderText(_translate("FormAddStudent", "Телефон"))
        self.label_2.setText(_translate("FormAddStudent", "Введите номер телефон"))
        self.edit_date_born.setPlaceholderText(_translate("FormAddStudent", "Дата рождения"))
        self.label_3.setText(_translate("FormAddStudent", "Введите дату рождения"))
        self.label_4.setText(_translate("FormAddStudent", "Группа студента"))
        self.edit_form_education.setPlaceholderText(_translate("FormAddStudent", "Форма образования"))
        self.label_5.setText(_translate("FormAddStudent", "Введите форму образования"))
        self.edit_place_residence.setPlaceholderText(_translate("FormAddStudent", "Место проживания"))
        self.label_6.setText(_translate("FormAddStudent", "Введите место проживания"))
        self.btn_add_student.setText(_translate("FormAddStudent", "Добавить студента"))
        self.label_7.setText(_translate("FormAddStudent", "Введите номер зачисления"))
        self.edit_enrollement_order.setPlaceholderText(_translate("FormAddStudent", "Номер зачисления"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormAddStudent = QtWidgets.QMainWindow()
    ui = Ui_FormAddStudent()
    ui.setupUi(FormAddStudent)
    FormAddStudent.show()
    sys.exit(app.exec_())
