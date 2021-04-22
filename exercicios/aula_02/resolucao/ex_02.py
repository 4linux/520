#!/usr/bin/python3


#1: criação da cesta de compras
cesta = []

frutas = {
  '1': 'Banana',
  '2': 'Melancia',
  '3': 'Morango'
}

#1: definição de menu interativo
while True:

#1.2 : apresentação do menu
    print(f'Quitanda\n' \
          f'1: Ver cesta\n' \
          f'2: Adicionar Frutas\n' \
          f'3: Sair')

#2: Captura opção desejada
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
        break

    else:
        print('Opção Inválida')

