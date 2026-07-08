import customtkinter as ctk

from database.database import Database
from ui.login import Login
from ui.main_window import SistemaNR35


class Aplicacao:
    def __init__(self):
        self.banco = Database()

        self.janela = ctk.CTk()
        self.configurar_janela()
        self.mostrar_login()

    def configurar_janela(self):
        self.janela.geometry("500x550")
        self.janela.title("SafeControl NR35")
        self.janela.resizable(False, False)

    def mostrar_login(self):
        self.limpar_janela()

        Login(
            master=self.janela,
            abrir_sistema=self.abrir_sistema
        )

    def abrir_sistema(self):
        self.janela.destroy()

        sistema = SistemaNR35()
        sistema.executar()

    def limpar_janela(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

    def executar(self):
        self.janela.mainloop()


if __name__ == "__main__":
    app = Aplicacao()
    app.executar()