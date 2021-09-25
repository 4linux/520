from caixa_eletronico import menus
from caixa_eletronico.bd import base


def main():
    base.criar_banco()
    menus.menu_principal()


if __name__ == '__main__':
    main()
