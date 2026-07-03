import customtkinter as ctk
from tkinter import messagebox


class Login(ctk.CTkFrame):

    def __init__(self, master, abrir_sistema):
        super().__init__(master)

        self.abrir_sistema = abrir_sistema
        self.pack(fill="both", expand=True)

        caixa = ctk.CTkFrame(self, width=420, height=430, corner_radius=20)
        caixa.place(relx=0.5, rely=0.5, anchor="center")
        caixa.pack_propagate(False)

        titulo = ctk.CTkLabel(
            caixa,
            text="🦺 SafeControl NR-35",
            font=("Arial", 28, "bold")
        )
        titulo.pack(pady=(45, 10))

        subtitulo = ctk.CTkLabel(
            caixa,
            text="Controle Inteligente de EPIs",
            font=("Arial", 15)
        )
        subtitulo.pack(pady=(0, 30))

        self.campo_usuario = ctk.CTkEntry(
            caixa,
            placeholder_text="Usuário",
            width=300,
            height=42
        )
        self.campo_usuario.pack(pady=10)

        self.campo_senha = ctk.CTkEntry(
            caixa,
            placeholder_text="Senha",
            width=300,
            height=42,
            show="*"
        )
        self.campo_senha.pack(pady=10)

        botao_entrar = ctk.CTkButton(
            caixa,
            text="ENTRAR",
            width=300,
            height=45,
            font=("Arial", 15, "bold"),
            command=self.validar_login
        )
        botao_entrar.pack(pady=25)

        rodape = ctk.CTkLabel(
            caixa,
            text="Versão 1.0 • Desenvolvido por Ryan Yuey",
            font=("Arial", 11)
        )
        rodape.pack(pady=(10, 0))

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