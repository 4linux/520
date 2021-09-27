from caixa_eletronico.menus.principal import menu_principal
from caixa_eletronico.bd import base


def main():
    base.criar_banco()
    menu_principal()


if __name__ == '__main__':
    main()
