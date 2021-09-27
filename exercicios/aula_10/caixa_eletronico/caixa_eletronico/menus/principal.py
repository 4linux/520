from getpass import getpass

from . import admin, cliente
from .. import exceptions, usuarios, contas


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
                    admin.menu_admin(u)

                else:
                    cliente.menu_cliente(u)

        elif escolha == 'S':
            print('Obrigado por usar o nosso sistema. Até logo!')
            break

        else:
            print('Por favor entre com uma opção válida.')
