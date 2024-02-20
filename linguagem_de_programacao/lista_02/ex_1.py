def main():
    try:
        resultado = numero + 10
    except NameError:
        print('Erro, variável não definida')
    else:
        print(resultado)
    finally:
        print('Operação finalizada!')

main()