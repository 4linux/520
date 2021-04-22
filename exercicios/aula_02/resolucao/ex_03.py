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

while True:

    print(f'Quitanda\n' \
          f'1: Ver cesta\n' \
          f'2: Adicionar Frutas\n' \
          f'3: Checkout\n' \
          f'4: Sair\n')

    op = input('Digite a opção desejada: ')

    if op == '1':
        print('Cesta de Compras:')
        for item in cesta:
            print(item)
            print('------------------------')

    elif op == '2':
        fruta = input(f'Escolha a fruta desejada:\n' \
                      f'1 - Banana\n' \
                      f'2 - Melancia\n' \
                      f'3 - Morango\n' \
                      f'Digite a opção desejada: ')
        if fruta in frutas:
            cesta.append(frutas[fruta])
            print(f'{frutas[fruta]} foi adicionado com sucesso!')
            print('------------------------')

        else:
            print('opção inválida')
            print('------------------------')
    elif op == '3':
        if len(cesta) > 0:
            total = 0
            for item in cesta:
                total += precos[item]

            print(f'Total de compras: {total}')
            print(f'Cesta de compras: {cesta}')
        else:
            print('Cesta de compras vazia.')

    elif op == '4':
        break

    else:
        print('Opção Inválida')

