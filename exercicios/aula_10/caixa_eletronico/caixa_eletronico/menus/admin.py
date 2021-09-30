from .. import exceptions, usuarios, contas

def menu_admin(admin: usuarios.Administrador):
    opcoes = {
        'C': 'Cadastrar novo cliente',
        'D': 'Desbloquear um cliente',
        'L': 'Fazer logout'
    }

    while True:
        print()
        print('=' * 10, 'MENU ADMINISTRATIVO', '=' * 10)

        for (op, descricao) in opcoes.items():
            print(f"{op} - {descricao}")

        escolha = input('Opção: ').strip().upper()

        if escolha == 'L':
            break

        elif escolha == 'C':
            username = input('Digite o username da nova conta: ')
            cadastrar_conta(admin, username)

        elif escolha == 'D':
            username = input('Digite o username da conta bloqueada: ')
            desbloquear_conta(admin, username)

        else:
            print('Por favor entre com uma opção válida.')


def cadastrar_conta(admin, username):
    if username == '':
        print('Username vazio.')
        return

    try:
        u = admin.criar(username)
        u.salvar()
        c = contas.Conta(u.id)
        c.salvar()
        print(f'Usuário `{username}` criado com sucesso.')
        print('A senha é o próprio username.')

    except exceptions.UsernameRepetido:
        raise


def desbloquear_conta(admin, username):
    try:
        admin.desbloquear(username)

    except exceptions.UsuarioInexistente:
        print("Username não consta no sistema.")

    else:
        print('Usuário desbloqueado com sucesso!')
        print('Senha resetada para o mesmo valor do username.')
