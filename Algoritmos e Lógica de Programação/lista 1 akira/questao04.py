#4) Faça um programa que calcule o aumento de um salário.
#   Ele deve solicitar o valor do salário e a porcentagem do aumento.
#   Exiba o valor do aumento e do novo salário.
print('Calcular aumento de salário')
print()

sal = float(input('digite o valor do salário:'))
aumento = float(input('digite o percentual de aumento:'))

print('o salário terá um aumento de $%.2f, ficando em $%.2f'
      %((sal * aumento / 100), (sal * aumento / 100)+sal))


