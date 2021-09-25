from . import exceptions
from .bd import contas


class Conta:
    def __init__(self, usuario_id, saldo=0.0, id=None):
        self.id = id
        self.usuario_id = usuario_id
        self.saldo = saldo

    def salvar(self):
        contas.salvar(self)

    def adicionar(self, quantia):
        if quantia < 0:
            raise exceptions.QuantiaInvalida

        self.saldo += quantia
        self.salvar()
        return self.saldo

    def retirar(self, quantia):
        if quantia < 0:
            raise exceptions.QuantiaInvalida

        if quantia > self.saldo:
            raise exceptions.SaldoInsuficiente

        self.saldo -= quantia
        self.salvar()
        return self.saldo


def buscar(usuario):
    acc_data = contas.buscar(usuario)

    if acc_data is None:
        # não deve acontecer, mas por via das dúvidas
        raise ValueError(f'Usuário {usuario.username} não possui conta associada')

    return Conta(*acc_data)
