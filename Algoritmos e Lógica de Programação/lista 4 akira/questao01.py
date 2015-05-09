'''
1. Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar 
as funções max e min.
'''
import random

lista = []
c = 1
maior = 1
menor = 100
while c <= 10:
    x = random.randint(1,100)
    lista.append(x)
    if x >= maior:
        maior = x
    if x <= menor:
        menor = x
    c += 1

print('Na lista %s o maior nº: %d menor nº: %d' %(lista,maior,menor))
