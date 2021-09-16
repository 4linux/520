

class Usuario:
    def __init__(self, username, senha,
                 bloqueado=True, primeira_senha=True,
                 tentativas_erradas=0, id=None):
        self.id = id
        self.username = username
        self.senha = senha
        self.bloqueado = bloqueado
        self.primeira_senha = primeira_senha
        self.tentativas_erradas = tentativas_erradas

    def salvar(self):
        pass

    @classmethod
    def carregar(cls, username, senha):
        return None


class Administrador(Usuario):
    def __init__(self, username, senha):
        super().__init__(username, senha, False, False)

    def desbloquear(self, usuario):
        pass


class Cliente(Usuario):
    pass
