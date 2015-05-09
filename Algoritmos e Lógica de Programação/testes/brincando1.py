spd = int(input('Qual a velocidade do seu carro?'))
if spd > 110:
    print("Voce ultrapassou ",spd-110,"km e foi multado em R$", (spd - 110)*5)
if spd < 110:
    print("velocidade dentro do permitido")

