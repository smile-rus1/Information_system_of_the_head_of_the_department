import os

from models.data_base import DATABASE_NAME, create_db, Session

from models.curator import Curator
from models.group import Group
from models.student import Student

from event.handler_question import handler_question
from event.handler_negative import handler_negative
from event.handler_possitive import handler_successful


def create_database():
    if not os.path.exists(DATABASE_NAME):
        if handler_question("Вы хотите создать базу данных?"):
            create_db()
            handler_successful("База данных была создана!")

        else:
            handler_negative("База данных не была создана")

    else:
        handler_negative("База данных уже создана!")

    session = Session()
    try:
        print("Connection...")

        session.commit()

    except Exception as ex:
        print(f"Exeption {ex}")
        session.rollback()

    finally:
        session.close()


if __name__ == '__main__':
    create_database()
