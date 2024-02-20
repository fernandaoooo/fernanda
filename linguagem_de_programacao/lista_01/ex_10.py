def leitura():
    n1 = float(input('Valor monetário: '))
    n2 = input('Tipo de moeda [RS-US-EU]: ').upper()
    return n1,n2

def conversao(dados):
    if dados[1] == 'RS':
        real = dados[0]
        dolar = dados[0] * 0.20
        euro = dados[0] * 0.19
    elif dados[1] == 'EU':
        euro = dados[0]
        real = dados[0] * 5.36
        dolar = dados[0] * 1.08
    elif dados[1] == 'US':
        dolar = dados[0]
        euro = dados[0] * 0.9219
        real = dados[0] * 4.94
    else:
        return 'Moeda não cadastrada!'
      
    return(f'R${real:.2f}\nU${dolar:.2f}\nEU{euro:.2f}')
        
while True:
    print(conversao(leitura()))
    continuar = input('Deseja continuar? ')
    if continuar != 'sim':
        break