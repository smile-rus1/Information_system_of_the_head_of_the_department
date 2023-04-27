from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMainWindow, QTableWidgetItem, QInputDialog, QLineEdit

from sqlalchemy import and_, func

from event.handler_negative import handler_negative
from event.handler_possitive import handler_successful
from event.handler_question import handler_question

from models.data_base import Session
from models.group import Group
from models.curator import Curator
from models.student import Student

from widjets.main_group_window import Ui_main_group_window

session = Session()


def filter_information(filter_text: str, operation: str) -> Group:
    try:
        if operation == "id":
            filter_operation = Group.id

        if operation == "Название группы":
            filter_operation = Group.name

        if operation == "Куратор":
            filter_operation = Curator.name

        info = session.query(Group.id, Group.name, Curator.name,
                func.ifnull(func.count(Student.group), 0)).join(Curator, Curator.id == Group.curator_id)\
            .outerjoin(Student, Student.group == Group.id)\
            .group_by(Group.name, Curator.name).filter(and_(filter_operation.like(f"%{filter_text}%")))

        return info

    except Exception as ex:
        handler_negative(ex)
        session.rollback()

    finally:
        session.close()


class FormMainGroup(QMainWindow, QDialog):
    global session

    def __init__(self, parent=None) -> None:
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
        self.ui_groups.btn_out_criteria_group.clicked.connect(lambda: self.show_filter_group())
        self.ui_groups.btn_delete_group.clicked.connect(lambda: self.delete_group())
        self.ui_groups.btn_save_change.clicked.connect(lambda: self.update_data())

    def check_combo(self) -> None:
        if self.ui_groups.cb_choice_filter.currentText() != "":
            self.ui_groups.edit_filter.setEnabled(True)
            self.ui_groups.edit_filter.setPlaceholderText("Введите данные")
        else:
            self.ui_groups.edit_filter.setEnabled(False)

    def show_all_info_group(self) -> None:
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

    def show_filter_group(self) -> None:
        if self.ui_groups.cb_choice_filter.currentText() == "":
            handler_negative("Вы не выбрали критерий выбора!")
            return

        if self.ui_groups.edit_filter.text() == "":
            handler_negative("Вы не написали данные")
            return

        self.ui_groups.table_all_groups.setRowCount(0)
        info = filter_information(self.ui_groups.edit_filter.text(), self.ui_groups.cb_choice_filter.currentText())
        self.ui_groups.table_all_groups.setRowCount(len(list(info)))

        for i, row in enumerate(info):
            rowtable = 0
            self.ui_groups.table_all_groups.setItem(i, 0, QTableWidgetItem(str(row[rowtable])))
            rowtable += 1
            self.ui_groups.table_all_groups.setItem(i, 1, QTableWidgetItem(str(row[rowtable])))
            rowtable += 1
            self.ui_groups.table_all_groups.setItem(i, 2, QTableWidgetItem(str(row[rowtable])))
            rowtable += 1
            self.ui_groups.table_all_groups.setItem(i, 3, QTableWidgetItem(str(row[rowtable])))

    def delete_group(self) -> None:
        try:
            text, pressed = QInputDialog.getText(self, "Введите Название группы, которую хотите удалить",
                                                 "Введите название", QLineEdit.Normal)
            if pressed and text != "":
                id_group = session.query(Group.id).filter(Group.name.like(f"{text}")).first()[0]
                group = session.query(Group).filter_by(id=id_group).first()

                session.delete(group)

                if handler_question(f"Вы действительно хотите удалить группу {group.name}?"):
                    session.commit()
                    handler_successful(f"Был удалена группа {group.name}")

                else:
                    session.rollback()
                    handler_successful("Данные не были удалены!")

        except:
            session.rollback()
            handler_negative("Не правильный ввод данных!")

        finally:
            session.close()

    def update_data(self) -> None:
        try:
            data_group = []

            for row in range(self.ui_groups.table_all_groups.rowCount()):
                rowdata = []
                for col in range(self.ui_groups.table_all_groups.columnCount()):
                    rowdata.append(self.ui_groups.table_all_groups.item(row, col).data(Qt.EditRole))

                data_group.append(tuple(rowdata))

            for i, dt in enumerate(data_group):
                st = 0
                data = []

                data.append(dt[st])
                st += 1
                data.append(dt[st])
                st += 1
                data.append(dt[st])

                group = session.query(Group).filter_by(id=int(data[0])).first()
                group.name = data[1]
                group.curator_id = session.query(Curator.id).filter(and_(Curator.name.like(f"{data[2]}"))).scalar_subquery()

            if handler_question("Вы действительно хотите сохранить?"):
                handler_successful("Данные успено сохранены!")
                session.commit()

            else:
                handler_successful("Данные не были сохранены!")
                session.rollback()

        except:
            session.rollback()
            handler_negative("Неверные данные!")

        finally:
            session.close()
