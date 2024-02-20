from banco import Banco

class Agencia:
    def __init__(self, numero) -> None:
        self.numero = numero
        banco = Banco('001','Banco da Amazônia')
        self.banco = banco