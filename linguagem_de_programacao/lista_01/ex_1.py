def num(n):
    if int(n) > 0:
        return 'P'
    elif int(n) == 0:
        return 'Z'
    else:
        return 'N'
    
print(num(float(input('Digite um número: '))))