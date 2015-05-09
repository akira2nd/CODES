#9) Escreva um programa que pergunte a quantidade de km percorridos por um carro
#   alugado pelo usuário, assim como a quantidade de dias pelos
#   quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro
#   custa R$ 60,00 por dia e R$ 0,15 por km rodado.
print('Calcular aluguel do carro')
print()

dias = int(input('Você vai alugar um carro,'
                 'por quantos dias pretende ficar com ele?:'))

km = int(input('Quantos Km irá percorrer?:'))

custo = (60 * dias) + (0.15 * km)

print('O aluguel do carro é R$60 o dia, acrescido de R$0,15 por km após entregue será cobrado o valor de R$ %.2f' %custo)
