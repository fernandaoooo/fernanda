def maior_de_idade(idade):
    if idade.isdecimal():
        if int(idade) < 18:
            return 'Menor de idade!'
        else:
            return 'Maior de idade!'
    else:
        return 'Número inválido!'
    
print(maior_de_idade(input('Digite sua idade: ')))