import sqlite3


class Database:

    def __init__(self):
        self.conexao = sqlite3.connect("database/nr35.db")
        self.cursor = self.conexao.cursor()
        self.criar_tabelas()

    def criar_tabelas(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS colaboradores(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                registro TEXT NOT NULL,
                setor TEXT NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS equipamentos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                ca TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                fabricante TEXT NOT NULL,
                validade TEXT NOT NULL,
                observacoes TEXT
            )
        """)

        self.conexao.commit()

    # ==========================
    # COLABORADORES
    # ==========================

    def cadastrar_colaborador(self, nome, registro, setor):
        self.cursor.execute("""
            INSERT INTO colaboradores (nome, registro, setor)
            VALUES (?, ?, ?)
        """, (nome, registro, setor))

        self.conexao.commit()

    def listar_colaboradores(self):
        self.cursor.execute("""
            SELECT *
            FROM colaboradores
            ORDER BY id ASC
        """)

        return self.cursor.fetchall()

    def pesquisar_colaboradores(self, termo):
        self.cursor.execute("""
            SELECT *
            FROM colaboradores
            WHERE nome LIKE ?
               OR registro LIKE ?
               OR setor LIKE ?
            ORDER BY id ASC
        """, (
            f"%{termo}%",
            f"%{termo}%",
            f"%{termo}%"
        ))

        return self.cursor.fetchall()

    def atualizar_colaborador(self, id_colaborador, nome, registro, setor):
        self.cursor.execute("""
            UPDATE colaboradores
            SET nome = ?, registro = ?, setor = ?
            WHERE id = ?
        """, (
            nome,
            registro,
            setor,
            id_colaborador
        ))

        self.conexao.commit()

    def excluir_colaborador(self, id_colaborador):
        self.cursor.execute("""
            DELETE FROM colaboradores
            WHERE id = ?
        """, (id_colaborador,))

        self.conexao.commit()

    # ==========================
    # EQUIPAMENTOS
    # ==========================

    def cadastrar_equipamento(
        self,
        nome,
        ca,
        quantidade,
        fabricante,
        validade,
        observacoes
    ):
        self.cursor.execute("""
            INSERT INTO equipamentos(
                nome,
                ca,
                quantidade,
                fabricante,
                validade,
                observacoes
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            nome,
            ca,
            quantidade,
            fabricante,
            validade,
            observacoes
        ))

        self.conexao.commit()

    def listar_equipamentos(self):
        self.cursor.execute("""
            SELECT
                id,
                nome,
                ca,
                quantidade,
                fabricante,
                validade
            FROM equipamentos
            ORDER BY id ASC
        """)

        return self.cursor.fetchall()