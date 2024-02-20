def num(*numeros:int):
    cont = 0 
    for n in numeros:
        if n > 0:
            cont+=1
    return cont

print(num(1,-7,6,5))