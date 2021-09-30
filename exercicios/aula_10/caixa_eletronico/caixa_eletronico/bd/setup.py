TABELA_USUARIOS = 'usuarios'
TABELA_CONTAS = 'contas'

config = {
    'banco': 'db.sqlite3',
    'tabelas': {
        TABELA_USUARIOS: [
            # Colunas no formato `nome TIPO`
            'username TEXT',
            'senha TEXT',
            'bloqueado INTEGER',
            'primeiro_acesso INTEGER',
            'tentativas_erradas INTEGER',
            'admin INTEGER'
        ],
        TABELA_CONTAS: [
            'usuario_id INTEGER',
            'saldo REAL'
        ]
    }
}
