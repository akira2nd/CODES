'''
7. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a 
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem 
compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.
'''
print('Calcular latas de tinta')
print()

metro = int(input('Informe o tamanho da área em metros quadrados: '))

litros = metro / 3
latas = (litros / 18)

if latas % 2 == 0:
    print('O total de latas a serem compradas é de: %d no valor de R$%.2f' %(latas, (int(latas)*80)))
else:
    print('O total de latas a serem compradas é de: %d no valor de R$%.2f' %(latas+1, ((int(latas)+1)*80)))
