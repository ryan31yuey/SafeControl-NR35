from database.database import Database
from ui.main_window import SistemaNR35


def main():

    Database()

    sistema = SistemaNR35()

    sistema.executar()


if __name__ == "__main__":
    main()