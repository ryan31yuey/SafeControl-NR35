from datetime import datetime
import customtkinter as ctk
from tkinter import messagebox

from assets.theme.theme import *
from database.database import Database
from ui.components import BotaoSecundario, TituloPagina


OPCAO_COLABORADOR = "Selecione o colaborador"
OPCAO_EQUIPAMENTO = "Selecione o equipamento"


class Estoque(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=BACKGROUND)

        self.banco = Database()

        self.pack(fill="both", expand=True)
        self.criar_interface()

    def criar_interface(self):
        TituloPagina(
            self,
            "Controle de Estoque",
            "Registre retiradas e devoluções de equipamentos."
        )

        self.criar_formulario()

    def criar_formulario(self):
        formulario = ctk.CTkFrame(
            self,
            width=620,
            height=380,
            corner_radius=18,
            fg_color=CARD
        )
        formulario.pack(pady=20)
        formulario.pack_propagate(False)

        self.combo_colaborador = ctk.CTkComboBox(
            formulario,
            values=self.banco.nomes_colaboradores(),
            width=450,
            height=40,
            state="readonly"
        )
        self.combo_colaborador.pack(pady=(35, 12))
        self.combo_colaborador.set(OPCAO_COLABORADOR)

        self.combo_equipamento = ctk.CTkComboBox(
            formulario,
            values=self.banco.nomes_equipamentos(),
            width=450,
            height=40,
            state="readonly",
            command=lambda valor: self.atualizar_estoque_atual()
        )
        self.combo_equipamento.pack(pady=12)
        self.combo_equipamento.set(OPCAO_EQUIPAMENTO)

        self.label_estoque = ctk.CTkLabel(
            formulario,
            text="Estoque atual: -",
            font=FONT_TEXT,
            text_color=TEXT_SECONDARY
        )
        self.label_estoque.pack(pady=(0, 8))

        self.campo_quantidade = ctk.CTkEntry(
            formulario,
            placeholder_text="Quantidade",
            width=450,
            height=40
        )
        self.campo_quantidade.pack(pady=12)

        self.criar_botoes(formulario)

    def criar_botoes(self, master):
        frame_botoes = ctk.CTkFrame(master, fg_color="transparent")
        frame_botoes.pack(pady=18)

        BotaoSecundario(
            frame_botoes,
            text="Retirar",
            width=180,
            command=self.retirar
        ).pack(side="left", padx=10)

        BotaoSecundario(
            frame_botoes,
            text="Devolver",
            width=180,
            command=self.devolver
        ).pack(side="left", padx=10)

    def atualizar_estoque_atual(self):
        equipamento = self.combo_equipamento.get()

        if equipamento == OPCAO_EQUIPAMENTO:
            self.label_estoque.configure(text="Estoque atual: -")
            return

        quantidade = self.banco.buscar_quantidade_equipamento(equipamento)

        if quantidade is None:
            self.label_estoque.configure(text="Estoque atual: -")
            return

        self.label_estoque.configure(text=f"Estoque atual: {quantidade}")

    def validar_campos(self):
        colaborador = self.combo_colaborador.get().strip()
        equipamento = self.combo_equipamento.get().strip()
        quantidade = self.campo_quantidade.get().strip()

        if colaborador == OPCAO_COLABORADOR:
            messagebox.showwarning("Atenção", "Selecione um colaborador.")
            return None

        if equipamento == OPCAO_EQUIPAMENTO:
            messagebox.showwarning("Atenção", "Selecione um equipamento.")
            return None

        if not quantidade:
            messagebox.showwarning("Atenção", "Informe a quantidade.")
            return None

        if not quantidade.isdigit() or int(quantidade) <= 0:
            messagebox.showwarning(
                "Atenção",
                "A quantidade deve ser um número maior que zero."
            )
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
        quantidade_atual = self.banco.buscar_quantidade_equipamento(equipamento)

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

        self.banco.alterar_quantidade(equipamento, nova_quantidade)

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

        self.finalizar_movimentacao()

    def devolver(self):
        dados = self.validar_campos()

        if dados is None:
            return

        colaborador, equipamento, quantidade = dados
        quantidade_atual = self.banco.buscar_quantidade_equipamento(equipamento)

        if quantidade_atual is None:
            messagebox.showerror("Erro", "Equipamento não encontrado.")
            return

        nova_quantidade = quantidade_atual + quantidade

        self.banco.alterar_quantidade(equipamento, nova_quantidade)

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

        self.finalizar_movimentacao()

    def finalizar_movimentacao(self):
        self.campo_quantidade.delete(0, "end")
        self.atualizar_estoque_atual()