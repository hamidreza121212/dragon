from sqlalchemy import create_engine

engin = create_engine("sqlite:///dragon_sqlite3.db", echo=True)

engin.connect()

from core import run_game


def main():
    run_game()


if __name__ == '__main__':
    main()


