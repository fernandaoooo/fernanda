class Veiculo:
    def __init__(self, cor, modelo, ano , marca, velocidade = 0) -> None:
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.marca = marca
        self.velocidade = velocidade
        print('Objeto do tipo Veiculo construído com sucesso!')

    def alterar_velocidade(self, valor):
        velocidade_atual = self.velocidade + valor
        if velocidade_atual < 0:
            print('INDISPONÍVEL')
        else:
            self.velocidade += valor

    def buzinar(self, valor:int):
        if valor == 1:
            print('Beep')
        elif valor == 2:
            print('BEEEEEP')
        else:
            print('Buzina estragada')