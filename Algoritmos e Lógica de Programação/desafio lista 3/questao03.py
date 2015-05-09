'''
3. Verifique se um inteiro positivo n é primo.
'''
print('Verificar se o número é primo')

n = int(input('Digite um número: '))
x = 2

while x < n:
    if n%x == 0:
        p = 'O número %d não é primo é divisivel por %d' %(n,x)
        break
    else:
        p = 'O número %d é primo' %n
    x += 1

print(p)
