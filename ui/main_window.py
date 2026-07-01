import customtkinter as ctk
from ui.dashboard import Dashboard
from ui.colaboradores import Colaboradores


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class SistemaNR35:

    def __init__(self):
        self.janela = ctk.CTk()
        self.janela.title("Sistema NR-35 PRO")
        self.janela.geometry("1200x700")
        self.janela.resizable(False, False)

        self.criar_layout()

    def criar_layout(self):
        self.topbar = ctk.CTkFrame(
            self.janela,
            height=70,
            corner_radius=0
        )
        self.topbar.pack(side="top", fill="x")

        titulo_topo = ctk.CTkLabel(
            self.topbar,
            text="Sistema NR-35 PRO",
            font=("Arial", 22, "bold")
        )
        titulo_topo.pack(side="left", padx=25)

        usuario = ctk.CTkLabel(
            self.topbar,
            text="Ryan Yuey",
            font=("Arial", 14)
        )
        usuario.pack(side="right", padx=25)

        self.corpo = ctk.CTkFrame(
            self.janela,
            corner_radius=0
        )
        self.corpo.pack(side="top", fill="both", expand=True)

        self.menu_lateral = ctk.CTkFrame(
            self.corpo,
            width=220,
            corner_radius=0
        )
        self.menu_lateral.pack(side="left", fill="y")

        self.area_principal = ctk.CTkFrame(
            self.corpo,
            corner_radius=0
        )
        self.area_principal.pack(side="right", fill="both", expand=True)

        self.criar_menu()
        Dashboard(self.area_principal)

    def criar_menu(self):
        titulo_menu = ctk.CTkLabel(
            self.menu_lateral,
            text="MENU",
            font=("Arial", 16, "bold")
        )
        titulo_menu.pack(pady=(25, 15))

        botoes = [
            ("🏠 Dashboard", lambda: self.trocar_tela(Dashboard)),
            ("👷 Colaboradores", lambda: self.trocar_tela(Colaboradores)),
            ("🦺 Equipamentos", lambda: print("Equipamentos")),
            ("📦 Estoque", lambda: print("Estoque")),
            ("📋 Histórico", lambda: print("Histórico")),
            ("📄 Relatórios", lambda: print("Relatórios")),
            ("⚙️ Configurações", lambda: print("Configurações")),
        ]

        for texto, comando in botoes:
            botao = ctk.CTkButton(
                self.menu_lateral,
                text=texto,
                width=180,
                height=40,
                anchor="w",
                command=comando
            )
            botao.pack(pady=8)

    def trocar_tela(self, Tela):
        for widget in self.area_principal.winfo_children():
            widget.destroy()

        Tela(self.area_principal)

    def executar(self):
        self.janela.mainloop()