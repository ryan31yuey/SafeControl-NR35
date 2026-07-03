import customtkinter as ctk
from tkinter import messagebox
from database.database import Database
from datetime import datetime


class Estoque(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.banco = Database()
        self.pack(fill="both", expand=True)

        titulo = ctk.CTkLabel(
            self,
            text="Controle de Estoque",
            font=("Arial", 28, "bold")
        )
        titulo.pack(pady=(40, 20))

        formulario = ctk.CTkFrame(self, width=600, height=320)
        formulario.pack(pady=20)
        formulario.pack_propagate(False)

        self.combo_colaborador = ctk.CTkComboBox(
            formulario,
            values=self.banco.nomes_colaboradores(),
            width=450,
            height=40
        )
        self.combo_colaborador.pack(pady=15)
        self.combo_colaborador.set("Selecione o colaborador")

        self.combo_equipamento = ctk.CTkComboBox(
            formulario,
            values=self.banco.nomes_equipamentos(),
            width=450,
            height=40
        )
        self.combo_equipamento.pack(pady=15)
        self.combo_equipamento.set("Selecione o equipamento")

        self.campo_quantidade = ctk.CTkEntry(
            formulario,
            placeholder_text="Quantidade",
            width=450,
            height=40
        )
        self.campo_quantidade.pack(pady=15)

        frame_botoes = ctk.CTkFrame(
            formulario,
            fg_color="transparent"
        )
        frame_botoes.pack(pady=20)

        ctk.CTkButton(
            frame_botoes,
            text="📤 Retirar",
            width=180,
            height=42,
            font=("Arial", 14, "bold"),
            command=self.retirar
        ).pack(side="left", padx=10)

        ctk.CTkButton(
            frame_botoes,
            text="📥 Devolver",
            width=180,
            height=42,
            font=("Arial", 14, "bold"),
            command=self.devolver
        ).pack(side="left", padx=10)

    def validar_campos(self):
        colaborador = self.combo_colaborador.get()
        equipamento = self.combo_equipamento.get()
        quantidade = self.campo_quantidade.get()

        if colaborador == "Selecione o colaborador":
            messagebox.showwarning("Atenção", "Selecione um colaborador.")
            return None

        if equipamento == "Selecione o equipamento":
            messagebox.showwarning("Atenção", "Selecione um equipamento.")
            return None

        if quantidade == "":
            messagebox.showwarning("Atenção", "Informe a quantidade.")
            return None

        if not quantidade.isdigit():
            messagebox.showwarning("Atenção", "A quantidade deve conter apenas números.")
            return None

        return colaborador, equipamento, int(quantidade)

    def registrar_movimentacao(self, colaborador, equipamento, quantidade, tipo):
        agora = datetime.now()
        data = agora.strftime("%d/%m/%Y")
        hora = agora.strftime("%H:%M:%S")

        self.banco.registrar_movimentacao(
            colaborador,
            equipamento,
            quantidade,
            tipo,
            data,
            hora
        )

    def retirar(self):
        dados = self.validar_campos()

        if dados is None:
            return

        colaborador, equipamento, quantidade = dados

        quantidade_atual = self.banco.buscar_quantidade_equipamento(
            equipamento
        )

        if quantidade_atual is None:
            messagebox.showerror("Erro", "Equipamento não encontrado.")
            return

        if quantidade > quantidade_atual:
            messagebox.showwarning(
                "Estoque insuficiente",
                f"Existem apenas {quantidade_atual} unidade(s) disponíveis."
            )
            return

        nova_quantidade = quantidade_atual - quantidade

        self.banco.alterar_quantidade(
            equipamento,
            nova_quantidade
        )

        self.registrar_movimentacao(
            colaborador,
            equipamento,
            quantidade,
            "Retirada"
        )

        messagebox.showinfo(
            "Sucesso",
            f"Retirada realizada!\n\nNovo estoque: {nova_quantidade}"
        )

        self.campo_quantidade.delete(0, "end")

    def devolver(self):
        dados = self.validar_campos()

        if dados is None:
            return

        colaborador, equipamento, quantidade = dados

        quantidade_atual = self.banco.buscar_quantidade_equipamento(
            equipamento
        )

        if quantidade_atual is None:
            messagebox.showerror("Erro", "Equipamento não encontrado.")
            return

        nova_quantidade = quantidade_atual + quantidade

        self.banco.alterar_quantidade(
            equipamento,
            nova_quantidade
        )

        self.registrar_movimentacao(
            colaborador,
            equipamento,
            quantidade,
            "Devolução"
        )

        messagebox.showinfo(
            "Sucesso",
            f"Devolução realizada!\n\nNovo estoque: {nova_quantidade}"
        )

        self.campo_quantidade.delete(0, "end")