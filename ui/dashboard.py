import customtkinter as ctk


class Dashboard(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.pack(fill="both", expand=True)

        titulo = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Arial", 30, "bold")
        )

        titulo.pack(pady=(40, 10))

        subtitulo = ctk.CTkLabel(
            self,
            text="Bem-vindo ao Sistema NR-35",
            font=("Arial", 18)
        )

        subtitulo.pack()