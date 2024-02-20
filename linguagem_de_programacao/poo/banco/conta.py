from abc import ABC, abstractmethod

class Conta(ABC):
    
    nr = 0

    def __init__(self, cliente, agencia, saldo=0) -> None:
        self.cliente = cliente
        Conta.nr += 1
        self.numero = Conta.nr
        self.agencia = agencia
        self.saldo = saldo

    #def depositar(valor:float) -> none:

    @abstractmethod
    def sacar(self, valor:float) -> bool: 
        pass
    #     if valor < 0:
    #         print('O valor não pode ser negativo')
    #         return False
    #     elif valor > self.saldo:
    #         print('Saldo insuficiente')
    #         return False
    #     else:
    #         self.saldo -= valor
    #         return True

    def depositar(self, valor:float):
        if valor < 0:
            print('O valor não pode ser negativo')
            return False
        else:
            self.saldo += valor
            return True

    def transferir(self, destinatario, valor: float) -> int:
        if self.sacar(valor):
            destinatario.depositar(valor)
            print('Transferência realizada com sucesso.')
        else:
            print('Transferência não realizada.')

