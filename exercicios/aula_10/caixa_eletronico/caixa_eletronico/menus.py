from getpass import getpass

from . import exceptions, usuarios, contas

def menu_principal():
    opcoes = {
        'L': 'Fazer login',
        'S': 'Sair e encerrar o programa'
    }

    while True:
        print()
        print('=' * 10, 'MENU PRINCIPAL', '=' * 10)
        print('Seja bem-vindo ao caixa automático. Selecione uma opção para continuar.')

        for (op, descricao) in opcoes.items():
            print(f"{op} - {descricao}")

        escolha = input('Opção: ').strip().upper()

        if escolha == 'L':
            username = input('Usuário: ')
            senha = getpass('Senha: ')

            try:
                u = usuarios.login(username, senha)

            except exceptions.UsuarioBloqueado:
                print('Usuário bloqueado - favor entrar em contato com a central.')

            except exceptions.CredenciaisInvalidas as ci:
                tentativas = ci.args[0]

                print('Credenciais inválidas.')
                if tentativas > 0:
                    print(f'Tentativas restantes antes do bloqueio de usuário: {3 - tentativas}')

            else:
                if u.admin:
                    menu_admin(u)

                else:
                    menu_usuario(u)

        elif escolha == 'S':
            print('Obrigado por usar o nosso sistema. Até logo!')
            break

        else:
            print('Por favor entre com uma opção válida.')



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

            if username == '':
                print('Username vazio.')
                continue

            try:
                u = admin.criar(username)
                u.salvar()
                c = contas.Conta(u.id)
                c.salvar()
                print(f'Usuário `{username}` criado com sucesso.')
                print('A senha é o próprio username.')

            except exceptions.UsernameRepetido:
                raise

        elif escolha == 'D':
            username = input('Digite o username da conta bloqueada: ')

            try:
                admin.desbloquear(username)

            except exceptions.UsuarioInexistente:
                print("Username não consta no sistema.")

            else:
                print('Usuário desbloqueado com sucesso!')
                print('Senha resetada para o mesmo valor do username.')

        else:
            print('Por favor entre com uma opção válida.')


def menu_usuario(cliente: usuarios.Cliente):
    if cliente.primeiro_acesso:
        trocar_senha(cliente)

    opcoes = {
        'C': 'Consultar o saldo',
        'S': 'Sacar uma quantia',
        'D': 'Depositar uma quantia',
        'T': 'Transferir para outra conta',
        'A': 'Alterar a senha',
        'L': 'Fazer logout'
    }

    while True:
        print()
        print('=' * 10, 'MENU DO USUÁRIO', '=' * 10)

        for (op, descricao) in opcoes.items():
            print(f"{op} - {descricao}")

        escolha = input('Opção: ').strip().upper()

        if escolha == 'L':
            break

        elif escolha == 'C':
            print(f'O seu saldo atual é de {cliente.get_saldo():.02f}')

        elif escolha == 'S':
            try:
                quantia = float(input('Digite a quantia a ser sacada: '))
                novo_saldo = cliente.sacar(quantia)

            except ValueError:
                print('Digite uma quantia válida.')

            except exceptions.SaldoInsuficiente:
                print('Saldo em conta insuficiente para saque.')

            except exceptions.QuantiaInvalida:
                print('Quantia inválida para saque.')

            else:
                print(f"Saque de {quantia:02f} realizado. Novo saldo: {novo_saldo:.02f}")

        elif escolha == 'D':
            try:
                quantia = float(input('Digite a quantia a ser depositada: '))
                novo_saldo = cliente.depositar(quantia)

            except ValueError:
                print('Digite uma quantia válida.')

            else:
                print(f"Depósito efetuado. Novo saldo em conta: {novo_saldo:.02f}")

        elif escolha == 'T':
            try:
                quantia = float(input('Digite a quantia a ser transferida: '))
                destinatario = input('Digite o username de destino: ')
                destinatario = usuarios.Cliente(*usuarios.usuarios.buscar(destinatario))
                (nsa, nsb) = cliente.transferir(quantia, destinatario)

            except ValueError:
                print('Digite uma quantia válida.')

            except TypeError:  # se a busca de username retornar None
                print('Usuário destinatário inválido.')

            except exceptions.QuantiaInvalida:
                print('Quantia inválida para realizar transferência.')

            except exceptions.SaldoInsuficiente:
                print('Saldo insuficiente para realizar transferência.')

            else:
                print('Transferência realizada!')
                print(f'Novo saldo do remetente: {nsa:.02f}')
                print(f'Novo saldo do destinatário: {nsb:.02f}')

        elif escolha == 'A':
            trocar_senha(cliente)

        else:
            print('Por favor entre com uma opção válida.')


def trocar_senha(cliente: usuarios.Cliente):
    senha, senha_conf = 'a', 'b'

    while senha != senha_conf:
        senha = getpass('Digite uma nova senha para a conta: ')
        senha_conf = getpass('Confirme a nova senha: ')

    cliente.senha = senha
    cliente.primeiro_acesso = False
    cliente.salvar()
