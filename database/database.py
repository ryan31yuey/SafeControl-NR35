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
            CREATE TABLE IF NOT EXISTS movimentacoes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                colaborador TEXT NOT NULL,
                equipamento TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                tipo TEXT NOT NULL,
                data TEXT NOT NULL,
                hora TEXT NOT NULL
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
        """, (nome, registro, setor, id_colaborador))
        self.conexao.commit()

    def excluir_colaborador(self, id_colaborador):
        self.cursor.execute("""
            DELETE FROM colaboradores
            WHERE id = ?
        """, (id_colaborador,))
        self.conexao.commit()

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

    def pesquisar_equipamentos(self, termo):
        self.cursor.execute("""
            SELECT
                id,
                nome,
                ca,
                quantidade,
                fabricante,
                validade
            FROM equipamentos
            WHERE nome LIKE ?
               OR ca LIKE ?
               OR fabricante LIKE ?
               OR validade LIKE ?
            ORDER BY id ASC
        """, (
            f"%{termo}%",
            f"%{termo}%",
            f"%{termo}%",
            f"%{termo}%"
        ))
        return self.cursor.fetchall()

    def atualizar_equipamento(
        self,
        id_equipamento,
        nome,
        ca,
        quantidade,
        fabricante,
        validade,
        observacoes
    ):
        self.cursor.execute("""
            UPDATE equipamentos
            SET
                nome = ?,
                ca = ?,
                quantidade = ?,
                fabricante = ?,
                validade = ?,
                observacoes = ?
            WHERE id = ?
        """, (
            nome,
            ca,
            quantidade,
            fabricante,
            validade,
            observacoes,
            id_equipamento
        ))

        self.conexao.commit()

    def excluir_equipamento(self, id_equipamento):
        self.cursor.execute("""
            DELETE FROM equipamentos
            WHERE id = ?
        """, (id_equipamento,))

        self.conexao.commit()

    def nomes_colaboradores(self):
        self.cursor.execute("""
            SELECT nome
            FROM colaboradores
            ORDER BY nome
        """)

        return [linha[0] for linha in self.cursor.fetchall()]

    def nomes_equipamentos(self):
        self.cursor.execute("""
            SELECT nome
            FROM equipamentos
            ORDER BY nome
        """)

        return [linha[0] for linha in self.cursor.fetchall()]

    def alterar_quantidade(self, nome_equipamento, nova_quantidade):
        self.cursor.execute("""
            UPDATE equipamentos
            SET quantidade = ?
            WHERE nome = ?
        """, (
            nova_quantidade,
            nome_equipamento
        ))

        self.conexao.commit()

    def buscar_quantidade_equipamento(self, nome_equipamento):
        self.cursor.execute("""
            SELECT quantidade
            FROM equipamentos
            WHERE nome = ?
        """, (nome_equipamento,))

        resultado = self.cursor.fetchone()

        if resultado is None:
            return None

        return resultado[0]

    def registrar_movimentacao(
        self,
        colaborador,
        equipamento,
        quantidade,
        tipo,
        data,
        hora
    ):
        self.cursor.execute("""
            INSERT INTO movimentacoes(
                colaborador,
                equipamento,
                quantidade,
                tipo,
                data,
                hora
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            colaborador,
            equipamento,
            quantidade,
            tipo,
            data,
            hora
        ))

        self.conexao.commit()