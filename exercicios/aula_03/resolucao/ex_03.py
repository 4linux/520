#!/usr/bin/python3

cesta = []

frutas = {
  '1': 'Banana',
  '2': 'Melancia',
  '3': 'Morango'
}

precos = {
  'Banana' : 3.50,
  'Melancia' : 7.50,
  'Morango': 5.00

}

def ver_cesta(lista_compras):
    if not esta_vazia(lista_compras):
        print('Cesta de Compras:')
        for item in cesta:
            print(item)
    else:
        print('Cesta de compras está vazia.')
    print('------------------------')

def adicionar_frutas(cesta_frutas):
    fruta = escolher_fruta()
    if fruta in frutas:
        cesta_frutas.append(frutas[fruta])
        print(f'{frutas[fruta]} foi adicionado com sucesso!')
        print('------------------------')

    else:
        print('Opção inválida')
        print('------------------------')


def escolher_fruta():
    return input(f'Escolha a fruta desejada:\n' \
                 f'1 - Banana\n' \
                 f'2 - Melancia\n' \
                 f'3 - Morango\n' \
                 f'Digite a opção desejada: ')

def checkout(cesta_frutas):
    if not esta_vazia(cesta_frutas):
        total = totalizar_precos(cesta_frutas)

        print(f'Total de compras: {total}')
        print(f'Cesta de compras: {cesta_frutas}')
    else:
        print('Cesta de compras vazia.')
    print('------------------------')


def esta_vazia(cesta_frutas):
    return len(cesta_frutas) == 0

def totalizar_precos(cesta_frutas):
    total = 0
    for item in cesta_frutas:
        total += precos[item]
    return total



def sair(*args):
    exit()


def main():
    while True:
        print(f'Quitanda\n' \
              f'1: Ver cesta\n' \
              f'2: Adicionar Frutas\n' \
              f'3: Checkout\n' \
              f'4: Sair\n')

        op = input('Digite a opção desejada: ')

        if op == '1':
            ver_cesta(cesta)
        elif op == '2':
            adicionar_frutas(cesta)
        elif op == '3':
            checkout(cesta)
        elif op == '4':
            sair()
        else:
            print('Opção Inválida')


if __name__ == '__main__':
    main()
