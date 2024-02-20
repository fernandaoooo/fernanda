def leitura():
    global n1, n2, n3 
    n1 = float(input('Digite a primeira medida do triângulo: '))
    n2 = float(input('Digite a segunda medida: '))
    n3 = float(input('Digite a terceira: '))
    verifica()

def verifica():
    if n1 > n2+n3 or n2 > n1+n3 or n3 > n1+n2:
        return False
    tipo()

def tipo():
    if n1 == n2 == n3:
        print('Triângulo Equilátero.')
    elif n1 == n2 or n1 == n3  or n2 == n3:
        print('Triângulo Isósceles.')
    else:
        print('Triângulo Escaleno.')
        
leitura()
        