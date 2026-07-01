import customtkinter as ctk


class Colaboradores(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.pack(fill="both", expand=True)

        titulo = ctk.CTkLabel(
            self,
            text="Cadastro de Colaboradores",
            font=("Arial", 28, "bold")
        )
        titulo.pack(pady=(40, 20))

        formulario = ctk.CTkFrame(self, width=500, height=350)
        formulario.pack(pady=20)
        formulario.pack_propagate(False)

        self.campo_nome = ctk.CTkEntry(
            formulario,
            placeholder_text="Nome do colaborador",
            width=400,
            height=40
        )
        self.campo_nome.pack(pady=15)

        self.campo_matricula = ctk.CTkEntry(
            formulario,
            placeholder_text="Matrícula / Registro",
            width=400,
            height=40
        )
        self.campo_matricula.pack(pady=15)

        self.campo_setor = ctk.CTkEntry(
            formulario,
            placeholder_text="Setor",
            width=400,
            height=40
        )
        self.campo_setor.pack(pady=15)

        botao_salvar = ctk.CTkButton(
            formulario,
            text="Salvar Colaborador",
            width=250,
            height=40,
            command=self.salvar_colaborador
        )
        botao_salvar.pack(pady=25)

    def salvar_colaborador(self):
        nome = self.campo_nome.get()
        matricula = self.campo_matricula.get()
        setor = self.campo_setor.get()

        print("Colaborador cadastrado:")
        print("Nome:", nome)
        print("Matrícula:", matricula)
        print("Setor:", setor)