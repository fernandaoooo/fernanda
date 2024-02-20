def num(n:int):
    n = list(str(n))
    n.reverse()
    return ''.join(n)
print(num(123))