import customtkinter as ctk

from assets.theme.theme import *


class BotaoPrimario(ctk.CTkButton):
    def __init__(self, master, text, command=None, width=330):
        super().__init__(
            master,
            text=text,
            command=command,
            width=width,
            height=48,
            corner_radius=RADIUS,
            fg_color=PRIMARY,
            hover_color=PRIMARY_HOVER,
            text_color=TEXT,
            font=FONT_TEXT
        )


class BotaoSecundario(ctk.CTkButton):
    def __init__(self, master, text, command=None, width=140):
        super().__init__(
            master,
            text=text,
            command=command,
            width=width,
            height=42,
            corner_radius=RADIUS,
            fg_color=CARD_DARK,
            hover_color=BORDER,
            text_color=TEXT,
            font=FONT_TEXT
        )


class BotaoPerigo(ctk.CTkButton):
    def __init__(self, master, text, command=None, width=140):
        super().__init__(
            master,
            text=text,
            command=command,
            width=width,
            height=42,
            corner_radius=RADIUS,
            fg_color=DANGER,
            hover_color=DANGER_HOVER,
            text_color=TEXT,
            font=FONT_TEXT
        )


class TituloPagina(ctk.CTkFrame):
    def __init__(self, master, titulo, subtitulo=None):
        super().__init__(master, fg_color="transparent")

        self.pack(fill="x", pady=(30, 15))

        ctk.CTkLabel(
            self,
            text=titulo,
            font=FONT_TITLE,
            text_color=TEXT
        ).pack()

        if subtitulo:
            ctk.CTkLabel(
                self,
                text=subtitulo,
                font=FONT_SUBTITLE,
                text_color=TEXT_SECONDARY
            ).pack(pady=(5, 0))


class CardDashboard(ctk.CTkFrame):
    def __init__(self, master, icone, titulo, valor):
        super().__init__(
            master,
            width=250,
            height=150,
            corner_radius=18,
            fg_color=CARD
        )

        self.pack_propagate(False)
        self.criar_conteudo(icone, titulo, valor)

    def criar_conteudo(self, icone, titulo, valor):
        topo = ctk.CTkFrame(self, fg_color="transparent")
        topo.pack(fill="x", padx=18, pady=(15, 5))

        ctk.CTkLabel(
            topo,
            text=icone,
            font=("Segoe UI Emoji", 26)
        ).pack(side="left")

        ctk.CTkLabel(
            topo,
            text=titulo,
            font=("Segoe UI", 15, "bold"),
            text_color=TEXT
        ).pack(side="left", padx=8)

        ctk.CTkFrame(
            self,
            height=2,
            fg_color=BORDER
        ).pack(fill="x", padx=18, pady=(5, 10))

        ctk.CTkLabel(
            self,
            text=str(valor),
            font=("Segoe UI", 34, "bold"),
            text_color=PRIMARY
        ).pack(expand=True)