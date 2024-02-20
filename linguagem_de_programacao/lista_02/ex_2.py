def divisao(a,b):
    try:
        resultado = a / b
    except TypeError:
        return 'Não é possível realizar a operação com string!'
    else:
        return resultado


print(divisao(10, 2))
print(divisao(10,'2'))