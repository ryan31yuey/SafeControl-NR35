import customtkinter as ctk
from database.database import Database


class Dashboard(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.banco = Database()

        self.pack(fill="both", expand=True)

        titulo = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Arial", 30, "bold")
        )
        titulo.pack(pady=(30, 10))

        subtitulo = ctk.CTkLabel(
            self,
            text="Bem-vindo ao SafeControl NR35",
            font=("Arial", 18)
        )
        subtitulo.pack(pady=(0, 25))

        frame_cards = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        frame_cards.pack(pady=10)

        self.criar_card(
            frame_cards,
            "👷 Colaboradores",
            self.banco.total_colaboradores(),
            0,
            0
        )

        self.criar_card(
            frame_cards,
            "🦺 Equipamentos",
            self.banco.total_equipamentos(),
            0,
            1
        )

        self.criar_card(
            frame_cards,
            "📦 Estoque Total",
            self.banco.total_estoque(),
            1,
            0
        )

        self.criar_card(
            frame_cards,
            "📤 Retiradas",
            self.banco.total_retiradas(),
            1,
            1
        )

        self.criar_card(
            frame_cards,
            "📥 Devoluções",
            self.banco.total_devolucoes(),
            2,
            0,
            columnspan=2
        )

    def criar_card(self, master, titulo, valor, linha, coluna, columnspan=1):

        card = ctk.CTkFrame(
            master,
            width=280,
            height=140,
            corner_radius=15
        )
        card.grid(
            row=linha,
            column=coluna,
            padx=20,
            pady=20,
            columnspan=columnspan
        )

        card.grid_propagate(False)

        ctk.CTkLabel(
            card,
            text=titulo,
            font=("Arial", 18, "bold")
        ).pack(pady=(25, 10))

        ctk.CTkLabel(
            card,
            text=str(valor),
            font=("Arial", 36, "bold")
        ).pack()