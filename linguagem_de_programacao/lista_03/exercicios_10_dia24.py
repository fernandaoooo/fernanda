from random import shuffle
from statistics import mean
from random import randint
 
def exercicio_01():
    ler = []
    for n in range(6):
        ler.append(int(input('Digite o valor: ')))
    print(ler)

# exercicio_01()

def exercicio_02():
    ler = []
    for n in range(10):
        ler.append(float(input('Digite o valor: ')))
    ler.sort()
    print(f'Menor número: {ler[0]}\nMaior número: {ler[-1]}')

# exercicio_02()

def exercicio_03():
    frutas = ['Maçã', 'Banana','Abacaxi','Manga','Mirtilo','Laranja','Uva','Banana','Abacate','Tomate']
    fruta = input('Digite o nome de uma fruta: ')
    print(f'Existe(m) {frutas.count(fruta)} {fruta}(s)')

# exercicio_03()

def exercicio_04():
    pessoas = ['Maria','Fernanda','Matheus','Ana','Jonas']
    shuffle(pessoas)
    print(pessoas)
    pessoas.sort()
    print(pessoas)

# exercicio_04()

def exercicio_05():
    notas = []
    for n in range(1,11):
        notas.append(float(input(f'Digite a {n}ª nota: ')))
    media = mean(notas)
    print(f'Média: {media}')

# exercicio_05()

def exercicio_06():
    num = []
    for n in range(1,9):
        while True:
            try:
                num.append(int(input(f'Digite o {n}º numero: ')))
                break
            except ValueError:
                print('Erro! Digite um número inteiro!')

    while True:
        try:
            x = int(input('Digite o primeiro índice: '))
            y = int(input('Digite o segundo índice: '))
            print (f'Os valores dos índices informados são: {num[x]} e {num[y]}')
            break
        except:
            print('Erro! Digite índices validos entre 0 a 7!')

    soma = num[x] + num[y]
    print(f'A soma dos numeros é {soma}')

# exercicio_06()

def exercicio_07():
    nomes = []
    for n in range(1,11):
        nomes.append(input(f'Digite o {n}º nome: '))
    tente = input('Digite um nome para verificar se está contido na lista: ')
    if tente in nomes: print('ACHEI')
    else: print('NÃO ACHEI')

# exercicio_07()

def exercicio_08():
    temperatura = []
    cont = 0
    for n in range(1,8):
        temperatura.append(float(input(f'Digite a {n}º temperatura: ')))
    media = mean(temperatura)
    print(f'A média das temperaturas informadas é {media}')
    for i in range(7):
        if temperatura[i] > media:
            cont =+ 1
            print(f'A temperatura de {cont} dia(s) foi acima da média')

# exercicio_08()

def exercicio_09():
    num = []
    while len(num)<=20:
        numero = randint(0,100)
        if numero not in num:
            num.append(numero)
    print(num)
    n = int(input('Digite um número entre 0 a 100: '))
    if n in num: print('Você ganhou!')
    else: print('Não foi desta vez!')

# exercicio_09()

def exercicio_10():
    num = int(input('Digite um número para saber sua tabuada: '))
    tabuada = [num * n for n in range(1,11)]
    print(tabuada)

# exercicio_10()