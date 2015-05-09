'''
2. Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os 
números ímpares na lista IMPAR. Imprima as três listas.
'''
import random

listaT = []
c = 1
while c <= 20:
    x = random.randint(1,100)
    listaT.append(x)
    c += 1

listaP = []
listaI = []
for c in listaT:
    if c%2 == 0:
        listaP.append(c)
    else:
        listaI.append(c)

print('lista Geral: ' ,listaT)
print('Lista Par: ' , listaP)
print('Lista Impar: ', listaI)
