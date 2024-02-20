def nome(n):
    nome = n.split(' ')
    if n.replace(' ','').isalpha() == True:
        return nome[0]
    else:
        return 'Erro'



print(nome('Matheus Albuquerque'))