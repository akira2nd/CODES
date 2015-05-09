'''
3. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa 
anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de 
crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos 
necessários para que a população do país A ultrapasse ou iguale a população do país B, 
mantidas as taxas de crescimento
'''
paisA = 80000
paisB = 200000
ano = 1

while paisA <= paisB:
    paisA += (paisA*0.03)
    paisB += (paisB*0.015)
    ano += 1

print('Em %d anos o país A terá uma população de %d, e o pais B %d habitantes' %(ano,paisA,paisB))
