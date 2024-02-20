def operacao(n1,n2,op):
    if op == '+':
        return (f'{int(n1)+int(n2)}')
    elif op == '-':
        return (f'{int(n1)-int(n2)}')
    elif op == '*':
        return (f'{int(n1)*int(n2)}')
    elif op == '/':
        return (f'{int(n1)/int(n2)}')
    else:
        return ('Operação inválida!')
print('Olá, seja bem vindo a Python Calculator!')
print(operacao(input('Digite o primeiro valor: '),input('Digite o segundo valor: '),input('Digite a operação desejada: ')))