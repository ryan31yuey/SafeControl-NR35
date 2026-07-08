import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "nr35.db"


class Database:
    def __init__(self):
        self.conexao = sqlite3.connect(DB_PATH)
        self.cursor = self.conexao.cursor()
        self.criar_tabelas()

    def criar_tabelas(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS colaboradores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                registro TEXT NOT NULL UNIQUE,
                setor TEXT NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS equipamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                ca TEXT NOT NULL,
                quantidade INTEGER NOT NULL DEFAULT 0,
                fabricante TEXT NOT NULL,
                validade TEXT NOT NULL,
                observacoes TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS movimentacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                colaborador TEXT NOT NULL,
                equipamento TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                tipo TEXT NOT NULL,
                data TEXT NOT NULL,
                hora TEXT NOT NULL
            )
        """)

        self.conexao.commit()

    def executar(self, sql, parametros=()):
        self.cursor.execute(sql, parametros)
        self.conexao.commit()

    def consultar(self, sql, parametros=()):
        self.cursor.execute(sql, parametros)
        return self.cursor.fetchall()

    def consultar_um(self, sql, parametros=()):
        self.cursor.execute(sql, parametros)
        return self.cursor.fetchone()

    # -------------------------
    # Colaboradores
    # -------------------------

    def cadastrar_colaborador(self, nome, registro, setor):
        self.executar("""
            INSERT INTO colaboradores (nome, registro, setor)
            VALUES (?, ?, ?)
        """, (nome.strip(), registro.strip(), setor.strip()))

    def listar_colaboradores(self):
        return self.consultar("""
            SELECT id, nome, registro, setor
            FROM colaboradores
            ORDER BY nome ASC
        """)

    def pesquisar_colaboradores(self, termo):
        termo = f"%{termo.strip()}%"

        return self.consultar("""
            SELECT id, nome, registro, setor
            FROM colaboradores
            WHERE nome LIKE ?
               OR registro LIKE ?
               OR setor LIKE ?
            ORDER BY nome ASC
        """, (termo, termo, termo))

    def atualizar_colaborador(self, id_colaborador, nome, registro, setor):
        self.executar("""
            UPDATE colaboradores
            SET nome = ?, registro = ?, setor = ?
            WHERE id = ?
        """, (
            nome.strip(),
            registro.strip(),
            setor.strip(),
            id_colaborador
        ))

    def excluir_colaborador(self, id_colaborador):
        self.executar("""
            DELETE FROM colaboradores
            WHERE id = ?
        """, (id_colaborador,))

    def nomes_colaboradores(self):
        registros = self.consultar("""
            SELECT nome
            FROM colaboradores
            ORDER BY nome ASC
        """)

        return [linha[0] for linha in registros]

    # -------------------------
    # Equipamentos
    # -------------------------

    def cadastrar_equipamento(
        self,
        nome,
        ca,
        quantidade,
        fabricante,
        validade,
        observacoes=""
    ):
        self.executar("""
            INSERT INTO equipamentos (
                nome,
                ca,
                quantidade,
                fabricante,
                validade,
                observacoes
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            nome.strip(),
            ca.strip(),
            int(quantidade),
            fabricante.strip(),
            validade.strip(),
            observacoes.strip()
        ))

    def listar_equipamentos(self):
        return self.consultar("""
            SELECT id, nome, ca, quantidade, fabricante, validade
            FROM equipamentos
            ORDER BY nome ASC
        """)

    def pesquisar_equipamentos(self, termo):
        termo = f"%{termo.strip()}%"

        return self.consultar("""
            SELECT id, nome, ca, quantidade, fabricante, validade
            FROM equipamentos
            WHERE nome LIKE ?
               OR ca LIKE ?
               OR fabricante LIKE ?
               OR validade LIKE ?
            ORDER BY nome ASC
        """, (termo, termo, termo, termo))

    def buscar_equipamento_por_id(self, id_equipamento):
        return self.consultar_um("""
            SELECT id, nome, ca, quantidade, fabricante, validade, observacoes
            FROM equipamentos
            WHERE id = ?
        """, (id_equipamento,))

    def atualizar_equipamento(
        self,
        id_equipamento,
        nome,
        ca,
        quantidade,
        fabricante,
        validade,
        observacoes=""
    ):
        self.executar("""
            UPDATE equipamentos
            SET nome = ?,
                ca = ?,
                quantidade = ?,
                fabricante = ?,
                validade = ?,
                observacoes = ?
            WHERE id = ?
        """, (
            nome.strip(),
            ca.strip(),
            int(quantidade),
            fabricante.strip(),
            validade.strip(),
            observacoes.strip(),
            id_equipamento
        ))

    def excluir_equipamento(self, id_equipamento):
        self.executar("""
            DELETE FROM equipamentos
            WHERE id = ?
        """, (id_equipamento,))

    def nomes_equipamentos(self):
        registros = self.consultar("""
            SELECT nome
            FROM equipamentos
            ORDER BY nome ASC
        """)

        return [linha[0] for linha in registros]

    def buscar_quantidade_equipamento(self, nome_equipamento):
        resultado = self.consultar_um("""
            SELECT quantidade
            FROM equipamentos
            WHERE nome = ?
        """, (nome_equipamento,))

        if resultado is None:
            return None

        return resultado[0]

    def alterar_quantidade(self, nome_equipamento, nova_quantidade):
        self.executar("""
            UPDATE equipamentos
            SET quantidade = ?
            WHERE nome = ?
        """, (int(nova_quantidade), nome_equipamento))

    # -------------------------
    # Estoque / Movimentações
    # -------------------------

    def registrar_movimentacao(
        self,
        colaborador,
        equipamento,
        quantidade,
        tipo,
        data,
        hora
    ):
        self.executar("""
            INSERT INTO movimentacoes (
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
            int(quantidade),
            tipo,
            data,
            hora
        ))

    def listar_movimentacoes(self):
        return self.consultar("""
            SELECT data, hora, colaborador, equipamento, tipo, quantidade
            FROM movimentacoes
            ORDER BY id DESC
        """)

    def ultimas_movimentacoes(self, limite=5):
        return self.consultar("""
            SELECT data, hora, colaborador, equipamento, tipo, quantidade
            FROM movimentacoes
            ORDER BY id DESC
            LIMIT ?
        """, (limite,))

    def pesquisar_movimentacoes(self, termo):
        termo = f"%{termo.strip()}%"

        return self.consultar("""
            SELECT data, hora, colaborador, equipamento, tipo, quantidade
            FROM movimentacoes
            WHERE colaborador LIKE ?
               OR equipamento LIKE ?
               OR tipo LIKE ?
               OR data LIKE ?
            ORDER BY id DESC
        """, (termo, termo, termo, termo))

    def limpar_movimentacoes(self):
        self.executar("""
            DELETE FROM movimentacoes
        """)

    # -------------------------
    # Dashboard
    # -------------------------

    def total_colaboradores(self):
        resultado = self.consultar_um("""
            SELECT COUNT(*)
            FROM colaboradores
        """)

        return resultado[0]

    def total_equipamentos(self):
        resultado = self.consultar_um("""
            SELECT COUNT(*)
            FROM equipamentos
        """)

        return resultado[0]

    def total_estoque(self):
        resultado = self.consultar_um("""
            SELECT COALESCE(SUM(quantidade), 0)
            FROM equipamentos
        """)

        return resultado[0]

    def total_retiradas(self):
        resultado = self.consultar_um("""
            SELECT COUNT(*)
            FROM movimentacoes
            WHERE tipo = 'Retirada'
        """)

        return resultado[0]

    def total_devolucoes(self):
        resultado = self.consultar_um("""
            SELECT COUNT(*)
            FROM movimentacoes
            WHERE tipo = 'Devolução'
        """)

        return resultado[0]

    def fechar(self):
        self.conexao.close()