'''
2. Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu 
algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando 
os centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que 
nenhuma delas esteja em falta no caixa.
'''
conta = int(input('Digite o valor da conta: '))
pagamento = int(input('Digite o valor do pagamento: '))

troco = (pagamento - conta)
cx = [50,20,10,5,2,1]
nt = ''
x = 0

while troco != 0:
    if troco < 0:
        print('Valora incorreto de pagamento!')
        break
    elif troco >= cx[x]:
        troco -= cx[x]
        nt += str(cx[x]) + ','
    else:
        x += 1

print('Notas necessárias para troco de R$%d: %s' %((pagamento - conta),nt))
