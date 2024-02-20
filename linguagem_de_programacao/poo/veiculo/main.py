from veiculo import Veiculo

ka = Veiculo('Rosa','Ka', 2020,'Ford')

print(ka.modelo,'Velocidade',ka.velocidade)
ka.alterar_velocidade(60)
print(ka.modelo,'Velocidade',ka.velocidade)
ka.alterar_velocidade(-10)
print(ka.modelo,'Velocidade',ka.velocidade)

ka.buzinar(3)