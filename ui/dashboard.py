import customtkinter as ctk

from database.database import Database
from assets.theme.theme import *
from ui.components import CardDashboard


class Dashboard(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.banco = Database()

        self.pack(fill="both", expand=True)
        self.configure(fg_color=BACKGROUND)

        titulo = ctk.CTkLabel(
            self,
            text="🛡 SafeControl",
            font=FONT_TITLE,
            text_color=PRIMARY
        )
        titulo.pack(pady=(25, 5))

        subtitulo = ctk.CTkLabel(
            self,
            text="Gestão Inteligente de EPIs",
            font=FONT_SUBTITLE,
            text_color=TEXT_SECONDARY
        )
        subtitulo.pack(pady=(0, 20))

        frame_cards = ctk.CTkFrame(self, fg_color="transparent")
        frame_cards.pack(pady=5)

        cards = [
            ("👷", "Colaboradores", self.banco.total_colaboradores()),
            ("🦺", "Equipamentos", self.banco.total_equipamentos()),
            ("📦", "Estoque Total", self.banco.total_estoque()),
            ("📤", "Retiradas", self.banco.total_retiradas()),
            ("📥", "Devoluções", self.banco.total_devolucoes()),
        ]

        for i, (icone, titulo_card, valor) in enumerate(cards):
            card = CardDashboard(
                frame_cards,
                icone=icone,
                titulo=titulo_card,
                valor=valor
            )

            linha = i // 2
            coluna = i % 2

            card.grid(
                row=linha,
                column=coluna,
                padx=18,
                pady=14
            )

        self.criar_ultimas_movimentacoes()

    def criar_ultimas_movimentacoes(self):
        painel = ctk.CTkFrame(
            self,
            width=560,
            height=190,
            corner_radius=18,
            fg_color=CARD
        )
        painel.pack(pady=(10, 20))
        painel.pack_propagate(False)

        titulo = ctk.CTkLabel(
            painel,
            text="🕒 Últimas Movimentações",
            font=("Segoe UI", 18, "bold"),
            text_color=TEXT
        )
        titulo.pack(anchor="w", padx=20, pady=(15, 10))

        movimentacoes = self.banco.ultimas_movimentacoes()

        if len(movimentacoes) == 0:
            vazio = ctk.CTkLabel(
                painel,
                text="Nenhuma movimentação registrada ainda.",
                font=FONT_TEXT,
                text_color=TEXT_SECONDARY
            )
            vazio.pack(pady=25)
            return

        for mov in movimentacoes:
            data, hora, colaborador, equipamento, tipo, quantidade = mov

            if tipo == "Retirada":
                icone = "📤"
                cor = PRIMARY
                texto = f"{hora} • {colaborador} retirou {quantidade}x {equipamento}"
            else:
                icone = "📥"
                cor = SUCCESS
                texto = f"{hora} • {colaborador} devolveu {quantidade}x {equipamento}"

            linha = ctk.CTkLabel(
                painel,
                text=f"{icone} {texto}",
                font=FONT_SMALL,
                text_color=cor
            )
            linha.pack(anchor="w", padx=25, pady=3)