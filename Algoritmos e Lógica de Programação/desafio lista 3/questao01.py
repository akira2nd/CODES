'''
1. Dizemos que um número natural é triangular se ele é produto de três números naturais 
consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, 
verificar se n é triangular.
'''
print('Verificar se o número é triangular')

numero = int(input('Digite um número: '))
x = 1
resp = 'O número não é triangular'
while (x*(x+1)*(x+2)) <= numero:
    if (x*(x+1)*(x+2)) == numero:
        resp = 'O número é triangular %d*%d*%d = %d'%(x,(x+1),(x+2), numero)
        
    x += 1
   
print(resp)
