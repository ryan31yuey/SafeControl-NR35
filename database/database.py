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
            ORDER BY id ASC
        """)

        return self.cursor.fetchall()

    def pesquisar_colaboradores(self, termo):
        self.cursor.execute("""
            SELECT * FROM colaboradores
            WHERE nome LIKE ?
               OR registro LIKE ?
               OR setor LIKE ?
            ORDER BY id ASC
        """, (f"%{termo}%", f"%{termo}%", f"%{termo}%"))

        return self.cursor.fetchall()

    def excluir_colaborador(self, id_colaborador):
        self.cursor.execute("""
            DELETE FROM colaboradores
            WHERE id = ?
        """, (id_colaborador,))

        self.conexao.commit()