'''
6. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule 
e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, 
quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os 
descontos e o salário líquido, conforme a tabela abaixo:
a. + Salário Bruto : R$
b. - IR (11%) : R$
c. - INSS (8%) : R$
d. - Sindicato ( 5%) : R$
e. = Salário Liquido : R$
'''

print('Consultar sálario')
print()

vhora = float(input('Informe o quanto você ganha por hora: '))
horames = int(input('Informe o quantidade de horas trabalhadas(mês): '))

salariob = vhora * horames
irenda = salariob * 0.11
inss = salariob * 0.08
sindic = salariob * 0.05
salariol = salariob - (irenda+inss+sindic)

print('Seu salário bruto:         R$', salariob)
print('Desconto Imposto de Renda: R$', irenda)
print('Dsconto INSS:              R$', inss)
print('Desconto Sindicato:        R$', sindic)
print('Total de descontos:        R$', (irenda+inss+sindic))
print('Líquido a receber:         R$', salariol)
