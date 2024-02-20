def main():
    print('Início do main')
    funcao_01()
    print('Fim do main')

def funcao_01():
    print('Início da função 01')
    funcao_02()
    print('Fim da função 01')

def funcao_02():
    print('Início da função 02')
    try:
        lista = range(10)
        for i in range(11):
            print(lista[i])
    except IndexError:
        print('Erro de índice!')

    print('Fim da função')

main()
