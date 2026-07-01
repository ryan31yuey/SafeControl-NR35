import customtkinter as ctk
from tkinter import messagebox
from tkinter import ttk
from database.database import Database


class Colaboradores(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.banco = Database()
        self.id_selecionado = None

        self.pack(fill="both", expand=True)

        titulo = ctk.CTkLabel(
            self,
            text="Cadastro de Colaboradores",
            font=("Arial", 28, "bold")
        )
        titulo.pack(pady=(30, 15))

        formulario = ctk.CTkFrame(self, width=500, height=320)
        formulario.pack(pady=10)
        formulario.pack_propagate(False)

        self.campo_nome = ctk.CTkEntry(
            formulario,
            placeholder_text="Nome do colaborador",
            width=400,
            height=40
        )
        self.campo_nome.pack(pady=12)

        self.campo_matricula = ctk.CTkEntry(
            formulario,
            placeholder_text="Matrícula / Registro",
            width=400,
            height=40
        )
        self.campo_matricula.pack(pady=12)

        self.campo_setor = ctk.CTkEntry(
            formulario,
            placeholder_text="Setor",
            width=400,
            height=40
        )
        self.campo_setor.pack(pady=12)

        frame_botoes = ctk.CTkFrame(
            formulario,
            fg_color="transparent"
        )
        frame_botoes.pack(pady=20)

        ctk.CTkButton(
            frame_botoes,
            text="💾 Salvar",
            width=120,
            command=self.salvar_colaborador
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            frame_botoes,
            text="✏ Atualizar",
            width=120,
            command=self.atualizar_colaborador
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            frame_botoes,
            text="🗑 Excluir",
            width=120,
            fg_color="#b71c1c",
            hover_color="#8e0000",
            command=self.excluir_colaborador
        ).pack(side="left", padx=5)

        self.campo_pesquisa = ctk.CTkEntry(
            self,
            placeholder_text="Pesquisar colaborador...",
            width=700,
            height=40
        )
        self.campo_pesquisa.pack(pady=(10, 5))
        self.campo_pesquisa.bind("<KeyRelease>", self.pesquisar)

        self.tabela = ttk.Treeview(
            self,
            columns=("id", "nome", "registro", "setor"),
            show="headings",
            height=8
        )

        self.tabela.heading("id", text="ID")
        self.tabela.heading("nome", text="Nome")
        self.tabela.heading("registro", text="Registro")
        self.tabela.heading("setor", text="Setor")

        self.tabela.column("id", width=60, anchor="center")
        self.tabela.column("nome", width=260)
        self.tabela.column("registro", width=150, anchor="center")
        self.tabela.column("setor", width=200)

        self.tabela.pack(pady=20)
        self.tabela.bind("<<TreeviewSelect>>", self.selecionar_colaborador)

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

        self.limpar_campos()
        self.atualizar_lista()

    def atualizar_colaborador(self):

        if self.id_selecionado is None:
            messagebox.showwarning(
                "Atenção",
                "Selecione um colaborador."
            )
            return

        nome = self.campo_nome.get()
        registro = self.campo_matricula.get()
        setor = self.campo_setor.get()

        if nome == "" or registro == "" or setor == "":
            messagebox.showwarning(
                "Atenção",
                "Preencha todos os campos."
            )
            return

        self.banco.atualizar_colaborador(
            self.id_selecionado,
            nome,
            registro,
            setor
        )

        messagebox.showinfo(
            "Sucesso",
            "Colaborador atualizado com sucesso!"
        )

        self.limpar_campos()
        self.atualizar_lista()

    def excluir_colaborador(self):

        if self.id_selecionado is None:
            messagebox.showwarning(
                "Atenção",
                "Selecione um colaborador."
            )
            return

        confirmar = messagebox.askyesno(
            "Excluir",
            "Deseja realmente excluir este colaborador?"
        )

        if confirmar:

            self.banco.excluir_colaborador(self.id_selecionado)

            messagebox.showinfo(
                "Sucesso",
                "Colaborador excluído."
            )

            self.limpar_campos()
            self.atualizar_lista()

    def atualizar_lista(self):

        for item in self.tabela.get_children():
            self.tabela.delete(item)

        colaboradores = self.banco.listar_colaboradores()

        for colaborador in colaboradores:
            self.tabela.insert(
                "",
                "end",
                values=colaborador
            )

    def pesquisar(self, evento):

        termo = self.campo_pesquisa.get()

        for item in self.tabela.get_children():
            self.tabela.delete(item)

        colaboradores = self.banco.pesquisar_colaboradores(termo)

        for colaborador in colaboradores:
            self.tabela.insert(
                "",
                "end",
                values=colaborador
            )

    def selecionar_colaborador(self, evento):

        selecionado = self.tabela.selection()

        if not selecionado:
            return

        dados = self.tabela.item(
            selecionado[0],
            "values"
        )

        self.id_selecionado = dados[0]

        self.campo_nome.delete(0, "end")
        self.campo_matricula.delete(0, "end")
        self.campo_setor.delete(0, "end")

        self.campo_nome.insert(0, dados[1])
        self.campo_matricula.insert(0, dados[2])
        self.campo_setor.insert(0, dados[3])

    def limpar_campos(self):

        self.id_selecionado = None

        self.campo_nome.delete(0, "end")
        self.campo_matricula.delete(0, "end")
        self.campo_setor.delete(0, "end")