from . import setup, base


QUERY_CRIACAO_CONTA = f"""
INSERT INTO {setup.TABELA_CONTAS} VALUES
(?, ?);
"""

QUERY_SELECAO_CONTA = f"""
SELECT *, rowid FROM {setup.TABELA_CONTAS} {{WHERE}};
"""

QUERY_ATUALIZACAO_CONTA = f"""
UPDATE {setup.TABELA_CONTAS} SET {{UPDATE}} WHERE rowid = ?;
"""


def buscar(usuario):
    acc_data = None
    where = 'WHERE usuario_id = ?'

    for con in base.criar_conexao():
        cursor = con.execute(QUERY_SELECAO_CONTA.format(WHERE=where),
                             (usuario.id,))

        acc_data = cursor.fetchone()

    return acc_data


def salvar(conta):
    id = conta.id

    for con in base.criar_conexao():
        dados = (conta.usuario_id, conta.saldo)

        if id is None:
            cursor = con.execute(QUERY_CRIACAO_CONTA, dados)
            conta.id = id = cursor.lastrowid

        else:
            update = ', '.join(['usuario_id = ?', 'saldo = ?'])
            dados += (id,)
            cursor = con.execute(QUERY_ATUALIZACAO_CONTA.format(UPDATE=update),
                                 dados)

        con.commit()
