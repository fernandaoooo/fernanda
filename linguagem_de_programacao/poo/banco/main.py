from cliente import Cliente
#from conta import Conta
from conta_corrente import ContaCorrente
from agencia import Agencia
import os
from conta_poupanca import ContaPoupanca


clientes = []
contas = []

def criar_clientes():
    clientes.append(Cliente('Matheus Albuquerque','065.104.601-49','(69) 99365-1904','Rua Barão do Rio Branco'))
    clientes.append(Cliente('Maria Fernanda Menezes','065.104.551-70','(69) 99365-1464','Avenida Major'))
    clientes.append(Cliente('Patricia Candida','717.851.751-00','(16) 99616-9602','Rua Liberdade'))

def print_clientes():
    for n in clientes:
        print(f'Nome: {n.nome}, CPF: {n.cpf}')
   

def criar_contas():
    agencia = Agencia('0001')
    contas.append(ContaCorrente(clientes[0],agencia, 13000000, 20000))
    contas.append(ContaCorrente(clientes[1],agencia, 30000000, 10000))
    contas.append(ContaCorrente(clientes[2],agencia, 12000000, 30000))
    contas.append(ContaPoupanca(clientes[0],agencia, 13000000))
    contas.append(ContaPoupanca(clientes[1],agencia, 30000000))
    contas.append(ContaPoupanca(clientes[2],agencia, 12000000))

def print_tudo():
    print('-'*100)
    for p in contas:
        print(f'Nome: {p.cliente.nome} | Conta: {p.numero} | Agência: {p.agencia.numero} | Banco: {p.agencia.banco.nome} | Saldo: {p.saldo}')
        if type(p) == ContaCorrente:
            print('|Conta Corrente')
        else: print('Conta Poupança')
        print('-'*100)

def encontrar_conta():
    while True:
        print_tudo()
        numero = int(input('Digite o número da conta: '))
        for conta in contas:
            if conta.numero == numero:
                return conta
        else:
            print('Conta não encontrada')

def main():
    criar_clientes()
    criar_contas()
    conta = encontrar_conta()
    while True:
        try:
            escolha = int(input('Digite a opção que deseja: 1- Mostrar lista de clientes; 2- Mostrar lista de contas; 3- Sacar; 4- Depositar; 5- Transferir; 9- Sair da aplicação.\nResposta: '))
            os.system('cls')
        except ValueError:
            print('Por favor, digite um número!')
        
        else:
            if escolha == 1: print_clientes()
            elif escolha == 2: print_tudo()
            elif escolha == 3: 
                valor = float(input('Insira o valor que deseja sacar: ')) 
                conta.sacar(valor)
            elif escolha == 4: 
                valor = (float(input('Insira o valor que deseja depositar: ')))
                conta.depositar(valor)
            elif escolha == 5:
                valor = (float(input('Insira o valor que deseja transferir: ')))
                destinatario = encontrar_conta()
                conta.transferir(valor, destinatario)
            elif escolha == 9: break
            else: print('Opção inválida!')
        

       

print('Seja bem-vindo!')
main()


#print(c1.__dict__)

# conta1 = Conta(c1,'1234')
# conta2 = Conta(c1,'1234')
# print(conta1.numero)
# print(conta2.numero)

