import customtkinter as ctk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk

from assets.theme.theme import *
from database.database import Database
from ui.components import BotaoPerigo, TituloPagina


SENHA_LIMPAR_HISTORICO = "admin123"


class Historico(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=BACKGROUND)

        self.banco = Database()

        self.pack(fill="both", expand=True)
        self.criar_interface()
        self.atualizar_lista()

    def criar_interface(self):
        TituloPagina(
            self,
            "Histórico de Movimentações",
            "Consulte retiradas e devoluções registradas no sistema."
        )

        self.criar_barra_acoes()
        self.criar_tabela()

    def criar_barra_acoes(self):
        barra = ctk.CTkFrame(self, fg_color="transparent")
        barra.pack(pady=(10, 5))

        self.campo_pesquisa = ctk.CTkEntry(
            barra,
            placeholder_text="Pesquisar por colaborador, equipamento, tipo ou data...",
            width=680,
            height=40
        )
        self.campo_pesquisa.pack(side="left", padx=(0, 10))
        self.campo_pesquisa.bind("<KeyRelease>", self.pesquisar)

        BotaoPerigo(
            barra,
            text="🗑 Limpar Histórico",
            width=170,
            command=self.confirmar_limpeza_historico
        ).pack(side="left")

    def criar_tabela(self):
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

        colunas = {
            "data": ("Data", 110, "center"),
            "hora": ("Hora", 100, "center"),
            "colaborador": ("Colaborador", 230, "w"),
            "equipamento": ("Equipamento", 230, "w"),
            "tipo": ("Tipo", 120, "center"),
            "quantidade": ("Qtd", 80, "center"),
        }

        for coluna, (titulo, largura, alinhamento) in colunas.items():
            self.tabela.heading(coluna, text=titulo)
            self.tabela.column(coluna, width=largura, anchor=alinhamento)

        self.tabela.pack(pady=20)

    def atualizar_lista(self):
        movimentacoes = self.banco.listar_movimentacoes()
        self.preencher_tabela(movimentacoes)

    def pesquisar(self, evento=None):
        termo = self.campo_pesquisa.get().strip()
        movimentacoes = self.banco.pesquisar_movimentacoes(termo)

        self.preencher_tabela(movimentacoes)

    def preencher_tabela(self, movimentacoes):
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        for movimentacao in movimentacoes:
            self.tabela.insert("", "end", values=movimentacao)

    def confirmar_limpeza_historico(self):
        if not self.banco.listar_movimentacoes():
            messagebox.showinfo(
                "Histórico vazio",
                "Não existem movimentações para limpar."
            )
            return

        confirmar = messagebox.askyesno(
            "Limpar histórico",
            "Deseja realmente apagar todo o histórico de movimentações?"
        )

        if not confirmar:
            return

        senha = simpledialog.askstring(
            "Confirmação",
            "Digite a senha para limpar o histórico:",
            show="*"
        )

        if senha is None:
            return

        if senha != SENHA_LIMPAR_HISTORICO:
            messagebox.showerror(
                "Senha incorreta",
                "A senha informada está incorreta."
            )
            return

        self.banco.limpar_movimentacoes()
        self.atualizar_lista()

        messagebox.showinfo(
            "Sucesso",
            "Histórico limpo com sucesso."
        )