import customtkinter as ctk

from database.database import Database
from ui.login import Login
from ui.main_window import SistemaNR35


class Aplicacao:

    def __init__(self):

        Database()

        self.janela = ctk.CTk()
        self.janela.geometry("500x550")
        self.janela.title("SafeControl NR35")
        self.janela.resizable(False, False)

        self.mostrar_login()

    def mostrar_login(self):

        for widget in self.janela.winfo_children():
            widget.destroy()

        Login(
            self.janela,
            self.abrir_sistema
        )

    def abrir_sistema(self):

        self.janela.destroy()

        sistema = SistemaNR35()
        sistema.executar()

    def executar(self):
        self.janela.mainloop()


if __name__ == "__main__":
    app = Aplicacao()
    app.executar()