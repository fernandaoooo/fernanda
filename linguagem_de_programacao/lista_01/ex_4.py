def num(*numeros:int):
    cont = 0 
    for n in numeros:
        if n % 2 == 0:
            cont+=1
    return cont

print(num(1,36,6,5))