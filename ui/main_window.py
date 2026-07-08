import customtkinter as ctk

from ui.dashboard import Dashboard
from ui.colaboradores import Colaboradores
from ui.equipamentos import Equipamentos
from ui.estoque import Estoque
from ui.historico import Historico
from ui.relatorios import Relatorios

from assets.theme.theme import *


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class SistemaNR35:

    def __init__(self):
        self.janela = ctk.CTk()
        self.janela.title("SafeControl")
        self.janela.geometry("1200x700")
        self.janela.resizable(False, False)

        self.botoes_menu = {}

        self.criar_layout()

    def criar_layout(self):
        self.topbar = ctk.CTkFrame(
            self.janela,
            height=70,
            corner_radius=0,
            fg_color=CARD_DARK
        )
        self.topbar.pack(side="top", fill="x")

        titulo_topo = ctk.CTkLabel(
            self.topbar,
            text="🛡 SafeControl",
            font=("Segoe UI", 24, "bold"),
            text_color=PRIMARY
        )
        titulo_topo.pack(side="left", padx=25)

        usuario = ctk.CTkLabel(
            self.topbar,
            text="Olá, Ryan Yuey 👋",
            font=FONT_TEXT,
            text_color=TEXT_SECONDARY
        )
        usuario.pack(side="right", padx=25)

        self.corpo = ctk.CTkFrame(
            self.janela,
            corner_radius=0,
            fg_color=BACKGROUND
        )
        self.corpo.pack(side="top", fill="both", expand=True)

        self.menu_lateral = ctk.CTkFrame(
            self.corpo,
            width=240,
            corner_radius=0,
            fg_color=CARD
        )
        self.menu_lateral.pack(side="left", fill="y")
        self.menu_lateral.pack_propagate(False)

        self.area_principal = ctk.CTkFrame(
            self.corpo,
            corner_radius=0,
            fg_color=BACKGROUND
        )
        self.area_principal.pack(side="right", fill="both", expand=True)

        self.criar_menu()
        self.trocar_tela(Dashboard, "Dashboard")

    def criar_menu(self):
        logo = ctk.CTkLabel(
            self.menu_lateral,
            text="🛡",
            font=("Segoe UI Emoji", 42)
        )
        logo.pack(pady=(25, 5))

        nome = ctk.CTkLabel(
            self.menu_lateral,
            text="SafeControl",
            font=("Segoe UI", 22, "bold"),
            text_color=PRIMARY
        )
        nome.pack()

        slogan = ctk.CTkLabel(
            self.menu_lateral,
            text="Gestão Inteligente de EPIs",
            font=("Segoe UI", 11),
            text_color=TEXT_SECONDARY
        )
        slogan.pack(pady=(0, 25))

        botoes = [
            ("Dashboard", "🏠  Dashboard", Dashboard),
            ("Colaboradores", "👷  Colaboradores", Colaboradores),
            ("Equipamentos", "🦺  Equipamentos", Equipamentos),
            ("Estoque", "📦  Estoque", Estoque),
            ("Histórico", "📋  Histórico", Historico),
            ("Relatórios", "📄  Relatórios", Relatorios),
        ]

        for nome_tela, texto, Tela in botoes:
            botao = ctk.CTkButton(
                self.menu_lateral,
                text=texto,
                width=200,
                height=42,
                corner_radius=12,
                anchor="w",
                font=FONT_TEXT,
                fg_color="transparent",
                hover_color=PRIMARY_HOVER,
                text_color=TEXT,
                command=lambda t=Tela, n=nome_tela: self.trocar_tela(t, n)
            )
            botao.pack(pady=6, padx=20)

            self.botoes_menu[nome_tela] = botao

        botao_config = ctk.CTkButton(
            self.menu_lateral,
            text="⚙️  Configurações",
            width=200,
            height=42,
            corner_radius=12,
            anchor="w",
            font=FONT_TEXT,
            fg_color="transparent",
            hover_color=PRIMARY_HOVER,
            text_color=TEXT,
            command=lambda: print("Configurações")
        )
        botao_config.pack(pady=6, padx=20)

        rodape = ctk.CTkLabel(
            self.menu_lateral,
            text="Versão 1.0",
            font=FONT_SMALL,
            text_color=TEXT_SECONDARY
        )
        rodape.pack(side="bottom", pady=20)

    def selecionar_menu(self, nome_tela):
        for botao in self.botoes_menu.values():
            botao.configure(fg_color="transparent")

        if nome_tela in self.botoes_menu:
            self.botoes_menu[nome_tela].configure(fg_color=PRIMARY)

    def trocar_tela(self, Tela, nome_tela):
        for widget in self.area_principal.winfo_children():
            widget.destroy()

        self.selecionar_menu(nome_tela)
        Tela(self.area_principal)

    def executar(self):
        self.janela.mainloop()