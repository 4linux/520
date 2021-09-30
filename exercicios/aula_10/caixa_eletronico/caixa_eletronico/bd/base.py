import sqlite3

from . import setup, usuarios


QUERY_CRIACAO_TABELA = """
CREATE TABLE {nome} (
    {colunas}
);
"""


def criar_conexao():
    con = sqlite3.connect(setup.config['banco'])
    yield con
    con.close()


def criar_banco():
    for con in criar_conexao():
        for (tabela, colunas) in setup.config['tabelas'].items():
            query = QUERY_CRIACAO_TABELA.format(nome=tabela, colunas=', '.join(colunas))

            try:
                con.execute(query)
                con.commit()

            except sqlite3.OperationalError:
                # tabela já existe
                pass

            else:
                if tabela == setup.TABELA_USUARIOS:
                    con.execute(usuarios.QUERY_CRIACAO_USUARIO,
                                ("root", "root", 0, 0, 0, 1))
