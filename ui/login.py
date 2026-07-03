import customtkinter as ctk
from tkinter import messagebox

from assets.theme.theme import *
from ui.components import BotaoPrimario


class Login(ctk.CTkFrame):

    def __init__(self, master, abrir_sistema):
        super().__init__(master)

        self.abrir_sistema = abrir_sistema

        self.pack(fill="both", expand=True)

        self.configure(fg_color=BACKGROUND)

        caixa = ctk.CTkFrame(
            self,
            width=460,
            height=520,
            corner_radius=18,
            fg_color=CARD
        )
        caixa.place(relx=0.5, rely=0.5, anchor="center")
        caixa.pack_propagate(False)

        logo = ctk.CTkLabel(
            caixa,
            text="🛡",
            font=("Segoe UI Emoji", 55)
        )
        logo.pack(pady=(25, 5))

        titulo = ctk.CTkLabel(
            caixa,
            text="SafeControl",
            font=FONT_TITLE,
            text_color=PRIMARY
        )
        titulo.pack()

        subtitulo = ctk.CTkLabel(
            caixa,
            text="Gestão Inteligente de EPIs",
            font=FONT_SUBTITLE,
            text_color=TEXT_SECONDARY
        )
        subtitulo.pack(pady=(0, 35))

        self.campo_usuario = ctk.CTkEntry(
            caixa,
            placeholder_text="👤 Usuário",
            width=330,
            height=45,
            corner_radius=10
        )
        self.campo_usuario.pack(pady=10)

        self.campo_senha = ctk.CTkEntry(
            caixa,
            placeholder_text="🔒 Senha",
            width=330,
            height=45,
            show="*",
            corner_radius=10
        )
        self.campo_senha.pack(pady=10)

        self.lembrar = ctk.CTkCheckBox(
            caixa,
            text="Lembrar usuário",
            font=FONT_TEXT
        )
        self.lembrar.pack(
            anchor="w",
            padx=65,
            pady=(5, 20)
        )

        botao = BotaoPrimario(
            caixa,
            text="ENTRAR",
            command=self.validar_login
        )
        botao.pack()

        versao = ctk.CTkLabel(
            caixa,
            text="Versão 1.0",
            font=FONT_SMALL,
            text_color=TEXT_SECONDARY
        )
        versao.pack(pady=(40, 0))

        autor = ctk.CTkLabel(
            caixa,
            text="Desenvolvido por Ryan Yuey",
            font=FONT_SMALL,
            text_color=TEXT_SECONDARY
        )
        autor.pack()

    def validar_login(self):
        usuario = self.campo_usuario.get()
        senha = self.campo_senha.get()

        if usuario == "admin" and senha == "123456":
            self.abrir_sistema()
        else:
            messagebox.showerror(
                "Erro",
                "Usuário ou senha inválidos."
            )