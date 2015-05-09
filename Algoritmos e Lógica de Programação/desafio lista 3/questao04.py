'''
4. Dado um número inteiro positivo, determine a sua decomposição em fatores primos 
calculando também a multiplicidade de cada fator.
'''
print('Decomposição em fatores primos')

n = int(input('Digite um número: '))

primo = []
a = 2
b = n
while b != 1:
    if b%a == 0 and b!=a:
        b -= 1
    elif b == a:
        primo.append(b)
        b -= 1
        a = 2
    else:
        a += 1

primo = primo[::-1]
x = 0
q = n
fat = []
while x < len(primo):
    if q % primo[x] == 0:
        print('%d / %d = %d' %(q,primo[x],(q/primo[x])))
        q /= primo[x]

        fat.append(primo[x])
        
    else:
        x += 1

print('Fatoração =', fat)

a = fat[0]
x = 1
while x < len(fat):
    print('%d * %d = %d' %(fat[x],a,(fat[x]*a)))
    a *= fat[x]
    x += 1



