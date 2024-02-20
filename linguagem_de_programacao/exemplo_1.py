# *** A questão a seguir está no nível de dificuldade da avaliação ***

# Crie um módulo que seja capaz de converter uma temperatura de Celsius para Fahrenheit e vise-versa:
# Organize o seu algorítmo em duas funções:

# A primeira função não possui parâmetro e será respondável pela leitura dos dados. O usuário deverá digitar dois valores,
# referentes à temperatura e à unidade de media. Obrigue o usuário a digitar valores aceitos nas duas variáveis
# e certifique-se que seu programa não irá travar em nenhuma situação. Esta função deverá retornar os valores lidos, separados por vírgula

# A segunda função será responsável por fazer a conversão da temperatura. Esta função receberá em uma única variável a temperatura e a unidade de medida.
# Caso a temperatura informada esteja em graus Celsius, deverá ser retornada a temperatura convertida para graus Fahrenheit.
# Caso a temperatura informada esteja em graus Fahrenheit, deverá ser retornada a temperatura convertida para graus Celsius

# Segue abaixo as fórmulas para conversão:
# Caso a temperatura informada esteja em Fahrenheit -> C = (F − 32.0) / 1.8
# Caso a temperatura informada esteja em Celsius -> F = C * 1.8 + 32
# sendo C a temperatura em Celsius e F a temperatura em Fahrenheit.

def ler_dados():  # 15 pontos
    while True:
        t = input('Digite uma temperatura: ')
        try:
            t = float(t)
        except ValueError:
            print('O valor digitado não foi aceito! Digite um número.')
        else:
            break

    while True:
        u = input('Em qual unidade de medida a temperatura fornecida se encontra[C-F]?').upper()
        if u == 'F' or u == 'C':
            break
        print('São aceitos somente os valores "F" ou "C".')

    return t, u


def conversor(dados): # 15 pontos
    if dados[1] == 'F':
        c = (dados[0] - 32.0) / 1.8  # Fahrenheit para Celsius
        return f'Temperatura convertida: {c:.2f}ºC'
    else:
        f = (dados[0] * 1.8 + 32)  # Celsius para Fahrenheit
        return f'Temperatura convertida: {f:.2f}ºF'


print(conversor(ler_dados())) # 5 pontos