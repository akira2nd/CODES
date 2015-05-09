'''
4. A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de 
formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a 
soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número 
de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.
'''
print('Números na sequencia de Fibonacci')

n = int(input('Digite um número: '))
F1 = 1
F2 = F1

while F1 <= n:
    if F1 <= n:
        print(F1)
    if F2 <= n:
        print(F2)

    F1 += F2 
    F2 += F1
    
