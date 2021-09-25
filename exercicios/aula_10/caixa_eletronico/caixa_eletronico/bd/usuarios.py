from . import setup, base


QUERY_CRIACAO_USUARIO = f"""
INSERT INTO {setup.TABELA_USUARIOS} VALUES
(?, ?, ?, ?, ?, ?);
"""

QUERY_SELECAO_USUARIO = f"""
SELECT *, rowid FROM {setup.TABELA_USUARIOS} {{WHERE}};
"""

QUERY_ATUALIZACAO_USUARIO = f"""
UPDATE {setup.TABELA_USUARIOS} SET {{UPDATE}} WHERE rowid = ?;
"""


def buscar(username):
    user_data = None
    where = 'WHERE username = ?'

    for con in base.criar_conexao():
        cursor = con.execute(QUERY_SELECAO_USUARIO.format(WHERE=where),
                             (username,))

        user_data = cursor.fetchone()

    return user_data


def salvar(usuario):
    id = usuario.id

    for con in base.criar_conexao():
        dados = (usuario.username, usuario.senha, usuario.bloqueado,
                 usuario.primeiro_acesso, usuario.tentativas_erradas,
                 usuario.admin)

        if id is None:  # criação de usuário
            cursor = con.execute(QUERY_CRIACAO_USUARIO, dados)
            usuario.id = id = cursor.lastrowid

        else:  # atualização de usuário
            update = ', '.join(['username = ?', 'senha = ?', 'bloqueado = ?',
                                'primeiro_acesso = ?', 'tentativas_erradas = ?', 'admin = ?'])
            dados += (id,)

            cursor = con.execute(QUERY_ATUALIZACAO_USUARIO.format(UPDATE=update),
                                 dados)

        con.commit()
