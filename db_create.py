import os

from models.data_base import DATABASE_NAME, create_db, Session
from models.curator import Curator
from models.group import Group
from models.student import Student


def main():
    if not os.path.exists(DATABASE_NAME):
        create_db()

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
    main()
