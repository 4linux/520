#!/usr/bin/python3

operacoes = {
    '1': lambda x,y: x+y,
    '2': lambda x,y: x-y,
    '3': lambda x,y: x/y if y != 0 else 'Não dividirás por zero.',
    '4': lambda x,y: x*y,
    '5': lambda x,y: exit()
}


def calculadora():
    while True:
        n1=float(input('N1: '))
        n2=float(input('N2: '))

        op = input(f'Operações:\n' \
             f'1 - Soma\n' \
             f'2 - Subtração\n' \
             f'3 - Divisão\n' \
             f'4 - Multiplicação\n'
             f'5 - Sair\n' \
             f'Digite a opção desejada: ')


        if op in operacoes:
            print(operacoes[op](n1,n2))
        else:
            print('Opção inválida')


if __name__ == '__main__':
    calculadora()
