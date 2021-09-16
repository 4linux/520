import sqlite3

from .config import config


QUERY_CRIACAO_TABELA = """
CREATE TABLE {nome} (
    {colunas}
);
"""


QUERY_CRIACAO_ADMIN = f"""
INSERT INTO {config['tabelas']['usuarios']} VALUES
("root", "root", 0, 0, 0);
"""


def criar_banco():
    tabelas = {
        config['tabelas']['usuarios']: [
            # Colunas no formato (nome, tipo)
            ('username', 'TEXT'),
            ('senha', 'TEXT'),
            ('bloqueado', 'INTEGER'),
            ('primeira_senha', 'INTEGER'),
            ('tentativas_erradas', 'INTEGER')
        ],
        config['tabelas']['contas']: [
            ('usuario_id', 'INTEGER'),
            ('saldo', 'REAL')
        ]
    }

    con = sqlite3.connect(config['banco'])

    for tabela in tabelas:
        colunas = []

        for coluna in tabelas[tabela]:
            colunas.append(' '.join(coluna))

        query = QUERY_CRIACAO_TABELA.format(nome=tabela, colunas=', '.join(colunas))

        try:
            con.execute(query)

        except sqlite3.OperationalError:
            # tabela já existe
            pass

        else:
            if tabela == config['tabelas']['usuarios']:
                con.execute(QUERY_CRIACAO_ADMIN)

    con.close()
