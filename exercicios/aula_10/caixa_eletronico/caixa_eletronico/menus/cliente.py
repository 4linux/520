from getpass import getpass

from .. import exceptions, usuarios, contas


def menu_cliente(cliente: usuarios.Cliente):
    if cliente.primeiro_acesso:
        alterar_senha(cliente)

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
            sacar(cliente)

        elif escolha == 'D':
            depositar(cliente)

        elif escolha == 'T':
            transferir(cliente)

        elif escolha == 'A':
            alterar_senha(cliente)

        else:
            print('Por favor entre com uma opção válida.')


def sacar(cliente):
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
        print(f"Saque de {quantia:.02f} realizado. Novo saldo: {novo_saldo:.02f}")


def depositar(cliente):
    try:
        quantia = float(input('Digite a quantia a ser depositada: '))
        novo_saldo = cliente.depositar(quantia)

    except ValueError:
        print('Digite uma quantia válida.')

    else:
        print(f"Depósito efetuado. Novo saldo em conta: {novo_saldo:.02f}")


def transferir(remetente):
    try:
        quantia = float(input('Digite a quantia a ser transferida: '))
        destinatario = input('Digite o username de destino: ')
        destinatario = usuarios.Cliente(*usuarios.usuarios.buscar(destinatario))  # noqa
        (nsa, nsb) = remetente.transferir(quantia, destinatario)

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


def alterar_senha(cliente: usuarios.Cliente):
    senha, senha_conf = 'a', 'b'

    while senha != senha_conf:
        senha = getpass('Digite uma nova senha para a conta: ')
        senha_conf = getpass('Confirme a nova senha: ')

    cliente.senha = senha
    cliente.primeiro_acesso = False
    cliente.salvar()
