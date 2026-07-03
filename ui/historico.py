import customtkinter as ctk
from tkinter import ttk
from database.database import Database


class Historico(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.banco = Database()

        self.pack(fill="both", expand=True)

        titulo = ctk.CTkLabel(
            self,
            text="Histórico de Movimentações",
            font=("Arial", 28, "bold")
        )
        titulo.pack(pady=(40, 20))

        self.campo_pesquisa = ctk.CTkEntry(
            self,
            placeholder_text="Pesquisar por colaborador, equipamento, tipo ou data...",
            width=850,
            height=40
        )
        self.campo_pesquisa.pack(pady=(10, 5))
        self.campo_pesquisa.bind("<KeyRelease>", self.pesquisar)

        self.tabela = ttk.Treeview(
            self,
            columns=(
                "data",
                "hora",
                "colaborador",
                "equipamento",
                "tipo",
                "quantidade"
            ),
            show="headings",
            height=18
        )

        self.tabela.heading("data", text="Data")
        self.tabela.heading("hora", text="Hora")
        self.tabela.heading("colaborador", text="Colaborador")
        self.tabela.heading("equipamento", text="Equipamento")
        self.tabela.heading("tipo", text="Tipo")
        self.tabela.heading("quantidade", text="Qtd")

        self.tabela.column("data", width=110, anchor="center")
        self.tabela.column("hora", width=100, anchor="center")
        self.tabela.column("colaborador", width=220)
        self.tabela.column("equipamento", width=220)
        self.tabela.column("tipo", width=120, anchor="center")
        self.tabela.column("quantidade", width=80, anchor="center")

        self.tabela.pack(pady=20)

        self.atualizar_lista()

    def atualizar_lista(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        movimentacoes = self.banco.listar_movimentacoes()

        for movimentacao in movimentacoes:
            self.tabela.insert(
                "",
                "end",
                values=movimentacao
            )

    def pesquisar(self, evento):
        termo = self.campo_pesquisa.get()

        for item in self.tabela.get_children():
            self.tabela.delete(item)

        movimentacoes = self.banco.pesquisar_movimentacoes(termo)

        for movimentacao in movimentacoes:
            self.tabela.insert(
                "",
                "end",
                values=movimentacao
            )