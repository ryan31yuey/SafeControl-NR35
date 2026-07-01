import customtkinter as ctk
from tkinter import messagebox
from database.database import Database


class Colaboradores(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.banco = Database()
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

        self.lista = ctk.CTkTextbox(
            self,
            width=700,
            height=180
        )
        self.lista.pack(pady=20)

        self.atualizar_lista()

    def salvar_colaborador(self):
        nome = self.campo_nome.get()
        registro = self.campo_matricula.get()
        setor = self.campo_setor.get()

        if nome == "" or registro == "" or setor == "":
            messagebox.showwarning(
                "Atenção",
                "Preencha todos os campos."
            )
            return

        self.banco.cadastrar_colaborador(nome, registro, setor)

        messagebox.showinfo(
            "Sucesso",
            "Colaborador cadastrado com sucesso!"
        )

        self.campo_nome.delete(0, "end")
        self.campo_matricula.delete(0, "end")
        self.campo_setor.delete(0, "end")

        self.atualizar_lista()

    def atualizar_lista(self):
        self.lista.delete("1.0", "end")

        colaboradores = self.banco.listar_colaboradores()

        self.lista.insert("end", "ID | Nome | Registro | Setor\n")
        self.lista.insert("end", "-" * 55 + "\n")

        for colaborador in colaboradores:
            texto = f"{colaborador[0]} | {colaborador[1]} | {colaborador[2]} | {colaborador[3]}\n"
            self.lista.insert("end", texto)