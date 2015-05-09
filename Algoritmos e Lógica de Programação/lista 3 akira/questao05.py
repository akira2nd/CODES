'''
5. Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando 
o algoritmo de Euclides.
'''
print('Calcular MDC de dois números')
print()

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = min(n1,n2)
r = (max(n1,n2) % n3)

print('Dividindo %d por %d o resto é: %d' %(max(n1,n2), n3,r))

while r != 0:
    print('Resto de %d / %d = %d' %(n3,r,(n3 % r)))
    n3,r = (r,n3%r)

print('O MDC é %d' %n3)
        
        
