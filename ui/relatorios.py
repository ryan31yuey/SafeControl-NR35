import customtkinter as ctk
from tkinter import messagebox
import os

from database.database import Database
from reports.pdf_generator import gerar_pdf_movimentacoes


class Relatorios(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.banco = Database()

        self.pack(fill="both", expand=True)

        titulo = ctk.CTkLabel(
            self,
            text="Relatórios",
            font=("Arial", 28, "bold")
        )
        titulo.pack(pady=(40, 20))

        descricao = ctk.CTkLabel(
            self,
            text="Gerar relatório completo das movimentações em PDF.",
            font=("Arial", 16)
        )
        descricao.pack(pady=(0, 30))

        ctk.CTkButton(
            self,
            text="📄 Gerar PDF",
            width=250,
            height=50,
            font=("Arial", 16, "bold"),
            command=self.gerar_pdf
        ).pack()

    def gerar_pdf(self):

        movimentacoes = self.banco.listar_movimentacoes()

        if len(movimentacoes) == 0:
            messagebox.showwarning(
                "Aviso",
                "Não existem movimentações cadastradas."
            )
            return

        arquivo = gerar_pdf_movimentacoes(movimentacoes)

        messagebox.showinfo(
            "Sucesso",
            f"Relatório gerado com sucesso!\n\n{arquivo}"
        )

        caminho_absoluto = os.path.abspath(arquivo)
        os.startfile(caminho_absoluto)