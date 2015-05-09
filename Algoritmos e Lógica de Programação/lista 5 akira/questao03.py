'''
Questão C. Entre 1067 e 3627 (inclusive), quantos números são pares e também 
divisíveis por 7? 
Resposta: 183
'''
x = 1067
cont = 0
while x <= 3627:
    if x % 2 == 0 and x % 7==0:
        cont += 1

    x = x + 1

print(cont)
