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

        self.conexao.commit()

    def cadastrar_colaborador(self, nome, registro, setor):
        self.cursor.execute("""
            INSERT INTO colaboradores (nome, registro, setor)
            VALUES (?, ?, ?)
        """, (nome, registro, setor))

        self.conexao.commit()

    def listar_colaboradores(self):
        self.cursor.execute("""
            SELECT * FROM colaboradores
            ORDER BY nome
        """)

        return self.cursor.fetchall()