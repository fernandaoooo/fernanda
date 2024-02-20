def verificar(idade:str):
    try:
        idade = int(idade)
    except ValueError:
        return 'Digite uma idade válida!'
    else:
        if idade > 17:
            return 'Maior de idade'
        else:
            return 'Menor de idade'

print(verificar(input('Digite sua idade: ')))