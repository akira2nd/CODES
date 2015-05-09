# 1. Faça um Programa que peça os três lados de um triângulo.
#   O programa deverá informar se os valores podem ser um triângulo.
#   Indique, caso os lados formem um triângulo, se o mesmo é:
#   equilátero, isósceles ou escaleno.
print('Lados de um triângulo')
print()

L1 = int(input('Digite um valor para o 1º lado do triangulo: '))
L2 = int(input('Digite um valor para o 2º lado do triangulo: '))
L3 = int(input('Digite um valor para o 3º lado do triangulo: '))

c = max(L1,L2,L3)
b = min(L1,L2,L3)
a = (L1+L2+L3)-(c+b)

if a==0 or b==0 or c==0: #verifica se foi digitádo algum valor nulo
    resultado = 'Com os dados informados não é possível ter um triângulo'
elif (a**2)+(b**2)==(c**2): #verifica soma do quadrado dos catetos se é diferente do quadrado da hipotenusa
    resultado = 'Com os dados informados você tem um TRIÂNGULO RETÂNGULO'
elif a == b == c:
    resultado = 'Seu triângulo é EQUILÁTERO todos os lados são iguais'
elif a == b or a == c or b == c:
    resultado = 'Seu triângulo é ISÓSCELES dois lados são iguais'
elif a != b and a!= c and b != c:
    resultado = 'Seu triângulo é ESCALENO todos os lados são diferentes'

print(resultado)
