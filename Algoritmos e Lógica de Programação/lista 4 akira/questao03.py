'''
3. Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um 
terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos 
intercalados dos dois outros vetores. Imprima os três vetores
'''
import random

listaA = []
for a in range(10):
    x = random.randint(1,100)
    listaA.append(x)


listaB = []
for a in range(10):
    x = random.randint(1,100)
    listaB.append(x)


listaAB = []
a = 0
while a < len(listaA):
    listaAB.append(listaA[a])
    listaAB.append(listaB[a])
    a += 1

print('Lista 1: ' ,listaA)
print('Lista 2: ' , listaB)
print('Lista 1e2: ', listaAB)
