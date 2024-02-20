from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, cliente, agencia, saldo=0) -> None:
        super().__init__(cliente, agencia, saldo)

    def sacar(self, valor):
        if valor <= 0:
            print('Valor inválido!')
            return False
        elif valor > self.saldo:
            print('Saldo insuficiente!')
            return False
        else:
            self.saldo -= valor
            return True