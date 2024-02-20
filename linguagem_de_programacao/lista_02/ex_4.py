def main():
    print('Vamos dividir!')
    while True:
        try:
            x = input('Digite o primeiro valor: ')
            x = int(x)
        except ValueError:
            print('Digite um número!') 
        else:
            break
    while True:  
        try:
            y = input('Digite o segundo valor: ')
            y = int(y)
            if y == 0:
                print('Não é possível dividir por 0!');continue
        except ValueError:
            print('Digite um número!') 
        else:
            break
    r = x/y
    print(f'O resultado da divisão é: {r}')

main()