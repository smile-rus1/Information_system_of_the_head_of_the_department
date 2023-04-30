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

from widjets.main_curator_window import Ui_main_curators_window

from modules_for_forms.form_add_curator import FormAddCurator
from modules_for_forms.form_change_group import FormChangeGroup


session = Session()


def filter_information(filter_text: str, operation: str) -> Curator:
    try:
        if operation == "id":
            filter_operation = Curator.id

        if operation == "ФИО":
            filter_operation = Curator.name

        if operation == "Группа":
            filter_operation = Group.name

        info = session.query(Curator.id, Curator.name, Group.name)\
            .join(Group, Curator.id == Group.curator_id)\
            .filter(and_(filter_operation.like(f"%{filter_text}%")))

        return info

    except Exception as ex:
        handler_negative(ex)
        session.rollback()

    finally:
        session.close()


class FormMainCurators(QMainWindow, QDialog):
    global session

    def __init__(self, parent=None) -> None:
        super(FormMainCurators, self).__init__(parent)
        self.ui_curators = Ui_main_curators_window()
        self.ui_curators.setupUi(self)

        self.setFixedHeight(465)
        self.setFixedWidth(665)

        self.ui_curators.table_all_curators.setColumnWidth(0, 10)
        self.ui_curators.table_all_curators.setColumnWidth(1, 100)
        self.ui_curators.table_all_curators.setColumnWidth(2, 100)

        self.ui_curators.cb_choice_filter.currentIndexChanged.connect(self.check_combo)
        self.ui_curators.btn_out_all_curators.clicked.connect(lambda: self.show_all_info_curators())
        self.ui_curators.btn_out_flter_data.clicked.connect(lambda: self.show_filter_curators())
        self.ui_curators.btn_delete_curator.clicked.connect(lambda: self.delete_curator())
        self.ui_curators.btn_save_change.clicked.connect(lambda: self.update_data())
        self.ui_curators.btn_open_add_curator_form.clicked.connect(lambda: FormAddCurator(self).show())
        self.ui_curators.btn_open_change_group.clicked.connect(lambda: FormChangeGroup(self).show())

    def check_combo(self) -> None:
        if self.ui_curators.cb_choice_filter.currentText() != "":
            self.ui_curators.edit_filter.setEnabled(True)
            self.ui_curators.edit_filter.setPlaceholderText("Введите данные")
        else:
            self.ui_curators.edit_filter.setEnabled(False)

    def show_all_info_curators(self) -> None:
        lst_info = [info for info in session.query(Curator.id, Curator.name, func.ifnull(Group.name, "Нет группы"))
            .outerjoin(Group, Group.curator_id == Curator.id).all()]

        self.ui_curators.table_all_curators.setRowCount(len(lst_info))

        for i, row in enumerate(lst_info):
            tablerow = 0
            self.ui_curators.table_all_curators.setItem(i, 0, QTableWidgetItem(str(row[tablerow])))
            tablerow += 1
            self.ui_curators.table_all_curators.setItem(i, 1, QTableWidgetItem(str(row[tablerow])))
            tablerow += 1
            self.ui_curators.table_all_curators.setItem(i, 2, QTableWidgetItem(str(row[tablerow])))

    def show_filter_curators(self) -> None:
        if self.ui_curators.cb_choice_filter.currentText() == "":
            handler_negative("Вы не выбрали критерий выбора!")
            return

        if self.ui_curators.edit_filter.text() == "":
            handler_negative("Вы не написали данные")
            return

        self.ui_curators.table_all_curators.setRowCount(0)
        info = filter_information(self.ui_curators.edit_filter.text(), self.ui_curators.cb_choice_filter.currentText())
        self.ui_curators.table_all_curators.setRowCount(len(list(info)))

        for i, row in enumerate(info):
            rowtable = 0
            self.ui_curators.table_all_curators.setItem(i, 0, QTableWidgetItem(str(row[rowtable])))
            rowtable += 1
            self.ui_curators.table_all_curators.setItem(i, 1, QTableWidgetItem(str(row[rowtable])))
            rowtable += 1
            self.ui_curators.table_all_curators.setItem(i, 2, QTableWidgetItem(str(row[rowtable])))

    def delete_curator(self) -> None:
        try:
            text, pressed = QInputDialog.getText(self, "Введите ФИО куратора, которого хотите удалить",
                                                 "Введите ФИО", QLineEdit.Normal)
            if pressed and text != "":
                id_curator = session.query(Curator.id).filter(Curator.name.like(f"{text}")).first()[0]
                curator = session.query(Curator).filter_by(id=id_curator).first()

                session.delete(curator)

                if handler_question(f"Вы действительно хотите удалить группу {curator.name}?"):
                    session.commit()
                    handler_successful(f"Был удалена группа {curator.name}")

                else:
                    session.rollback()
                    handler_successful("Данные не были удалены!")

        except:
            session.rollback()
            handler_negative("Не правильный ввод данных!")

        finally:
            session.close()

    def update_data(self):
        try:
            data_curator = []

            for row in range(self.ui_curators.table_all_curators.rowCount()):
                rowdata = []
                for col in range(self.ui_curators.table_all_curators.columnCount()):
                    rowdata.append(self.ui_curators.table_all_curators.item(row, col).data(Qt.EditRole))

                data_curator.append(tuple(rowdata))

            for i, dt in enumerate(data_curator):
                st = 0
                data = []

                data.append(dt[st])
                st += 1
                data.append(dt[st])
                st += 1
                data.append(dt[st])

                curator = session.query(Curator).filter_by(id=int(data[0])).first()
                curator.name = data[1]

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
