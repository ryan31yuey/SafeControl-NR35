import customtkinter as ctk
from tkinter import messagebox
from tkinter import ttk
from database.database import Database


class Equipamentos(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.banco = Database()
        self.id_selecionado = None

        self.pack(fill="both", expand=True)

        titulo = ctk.CTkLabel(
            self,
            text="Gestão de Equipamentos",
            font=("Arial", 28, "bold")
        )
        titulo.pack(pady=(25, 10))

        formulario = ctk.CTkFrame(self, width=700, height=410)
        formulario.pack(pady=10)
        formulario.pack_propagate(False)

        self.campo_nome = ctk.CTkEntry(
            formulario,
            placeholder_text="Nome do equipamento",
            width=560,
            height=38
        )
        self.campo_nome.pack(pady=8)

        self.campo_ca = ctk.CTkEntry(
            formulario,
            placeholder_text="Número do CA",
            width=560,
            height=38
        )
        self.campo_ca.pack(pady=8)

        self.campo_quantidade = ctk.CTkEntry(
            formulario,
            placeholder_text="Quantidade",
            width=560,
            height=38
        )
        self.campo_quantidade.pack(pady=8)

        self.campo_fabricante = ctk.CTkEntry(
            formulario,
            placeholder_text="Fabricante",
            width=560,
            height=38
        )
        self.campo_fabricante.pack(pady=8)

        self.campo_validade = ctk.CTkEntry(
            formulario,
            placeholder_text="Data de validade do CA",
            width=560,
            height=38
        )
        self.campo_validade.pack(pady=8)

        self.campo_observacoes = ctk.CTkEntry(
            formulario,
            placeholder_text="Observações",
            width=560,
            height=38
        )
        self.campo_observacoes.pack(pady=8)

        frame_botoes = ctk.CTkFrame(
            formulario,
            fg_color="transparent"
        )
        frame_botoes.pack(pady=12)

        ctk.CTkButton(
            frame_botoes,
            text="💾 Salvar",
            width=150,
            height=42,
            font=("Arial", 14, "bold"),
            command=self.salvar_equipamento
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            frame_botoes,
            text="✏ Atualizar",
            width=150,
            height=42,
            font=("Arial", 14, "bold"),
            command=self.atualizar_equipamento
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            frame_botoes,
            text="🗑 Excluir",
            width=150,
            height=42,
            font=("Arial", 14, "bold"),
            fg_color="#b71c1c",
            hover_color="#8e0000",
            command=self.excluir_equipamento
        ).pack(side="left", padx=5)

        self.campo_pesquisa = ctk.CTkEntry(
            self,
            placeholder_text="Pesquisar equipamento...",
            width=850,
            height=40
        )
        self.campo_pesquisa.pack(pady=(10, 5))

        self.tabela = ttk.Treeview(
            self,
            columns=("id", "nome", "ca", "quantidade", "fabricante", "validade"),
            show="headings",
            height=9
        )

        self.tabela.heading("id", text="ID")
        self.tabela.heading("nome", text="Equipamento")
        self.tabela.heading("ca", text="CA")
        self.tabela.heading("quantidade", text="Qtd")
        self.tabela.heading("fabricante", text="Fabricante")
        self.tabela.heading("validade", text="Validade")

        self.tabela.column("id", width=50, anchor="center")
        self.tabela.column("nome", width=220)
        self.tabela.column("ca", width=110, anchor="center")
        self.tabela.column("quantidade", width=80, anchor="center")
        self.tabela.column("fabricante", width=160)
        self.tabela.column("validade", width=140, anchor="center")

        self.tabela.pack(pady=15)

        self.atualizar_lista()

    def salvar_equipamento(self):
        nome = self.campo_nome.get()
        ca = self.campo_ca.get()
        quantidade = self.campo_quantidade.get()
        fabricante = self.campo_fabricante.get()
        validade = self.campo_validade.get()
        observacoes = self.campo_observacoes.get()

        if nome == "" or ca == "" or quantidade == "" or fabricante == "" or validade == "":
            messagebox.showwarning(
                "Atenção",
                "Preencha todos os campos obrigatórios."
            )
            return

        if not quantidade.isdigit():
            messagebox.showwarning(
                "Atenção",
                "A quantidade deve conter apenas números."
            )
            return

        self.banco.cadastrar_equipamento(
            nome,
            ca,
            int(quantidade),
            fabricante,
            validade,
            observacoes
        )

        messagebox.showinfo(
            "Sucesso",
            "Equipamento cadastrado com sucesso!"
        )

        self.limpar_campos()
        self.atualizar_lista()

    def atualizar_lista(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        equipamentos = self.banco.listar_equipamentos()

        for equipamento in equipamentos:
            self.tabela.insert(
                "",
                "end",
                values=equipamento
            )

    def limpar_campos(self):
        self.id_selecionado = None
        self.campo_nome.delete(0, "end")
        self.campo_ca.delete(0, "end")
        self.campo_quantidade.delete(0, "end")
        self.campo_fabricante.delete(0, "end")
        self.campo_validade.delete(0, "end")
        self.campo_observacoes.delete(0, "end")

    def atualizar_equipamento(self):
        messagebox.showinfo(
            "Em desenvolvimento",
            "Função Atualizar Equipamento será implementada depois."
        )

    def excluir_equipamento(self):
        messagebox.showinfo(
            "Em desenvolvimento",
            "Função Excluir Equipamento será implementada depois."
        )