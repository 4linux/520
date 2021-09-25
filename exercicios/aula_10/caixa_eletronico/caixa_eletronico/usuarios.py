from . import exceptions, contas
from .bd import usuarios


class Usuario:
    def __init__(self, username, senha,
                 bloqueado=True, primeiro_acesso=True,
                 tentativas_erradas=0, admin=False, id=None):
        self.id = id
        self.username = username
        self.senha = senha
        self.bloqueado = bloqueado
        self.primeiro_acesso = primeiro_acesso
        self.tentativas_erradas = tentativas_erradas
        self.admin = admin

    def salvar(self):
        usuarios.salvar(self)


class Administrador(Usuario):
    def __init__(self, username, senha, id=None):
        super().__init__(username, senha, False, False, admin=True, id=id)

    def criar(self, username):
        if usuarios.buscar(username) is not None:
            raise exceptions.UsernameRepetido

        return Cliente(username, username)

    def desbloquear(self, username):
        user_data = usuarios.buscar(username)

        if user_data is None:
            raise exceptions.UsuarioInexistente

        u = Usuario(*user_data)
        u.senha = u.username
        u.bloqueado = False
        u.primeiro_acesso = True
        u.tentativas_erradas = 0
        u.salvar()


class Cliente(Usuario):
    def get_conta(self):
        return contas.buscar(self)

    def get_saldo(self):
        return self.get_conta().saldo

    def sacar(self, quantia):
        return self.get_conta().retirar(quantia)

    def depositar(self, quantia):
        return self.get_conta().adicionar(quantia)

    def transferir(self, quantia, destinatario):
        novo_saldo_a = self.sacar(quantia)
        novo_saldo_b = destinatario.depositar(quantia)
        return (novo_saldo_a, novo_saldo_b)


def login(username, senha):
    user_data = usuarios.buscar(username)

    if user_data is None:
        raise exceptions.CredenciaisInvalidas(-1)

    u = Usuario(*user_data)

    if u.bloqueado:
        raise exceptions.UsuarioBloqueado

    if senha != u.senha:
        u.tentativas_erradas += 1

        if u.tentativas_erradas == 3:
            u.bloqueado = True

        u.salvar()
        raise exceptions.CredenciaisInvalidas(u.tentativas_erradas)

    if u.admin:
        u = Administrador(u.username, u.senha, u.id)

    else:
        u = Cliente(*user_data)

    u.tentativas_erradas = 0
    u.salvar()
    return u
