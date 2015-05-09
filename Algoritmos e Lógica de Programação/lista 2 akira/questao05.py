'''
5. Faça um Programa que leia três números e mostre o maior e o menor deles.
'''
print('Verificar maior e menor de 3 números')
print()

n1 = int(input('Digite 1º número: '))
n2 = int(input('Digite 2º número: '))
n3 = int(input('Digite 3º número: '))

print('O maior valor digitado foi %d e o menor %d' %(max(n1,n2,n3),min(n1,n2,n3)))
