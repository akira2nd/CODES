#6) Calcule o tempo de uma viagem de carro.
#   Pergunte a distância a percorrer e a
#   velocidade média esperada para a viagem.
print('Calcular tempo de viagem')
print()

distancia = float(input('digite a distancia que irá percorrer(km):'))
velo = float(input('digite a velocidade média que ira viajar(km/h):'))

temp = distancia / velo

print('O tempo de viagem estimado é de: %.2f horas' %temp)
