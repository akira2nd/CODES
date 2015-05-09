#5) Solicite o preço de uma mercadoria e o percentual de desconto.
#   Exiba o valor do desconto e o preço a pagar.

merc = float(input('digite o valor da mercadoria:'))
desc = float(input('digite o percentual de desconto:'))

print('a mercadoria terá um desconto de $%.2f, valor final = $%.2f'
      %((merc * desc / 100), merc-(merc * desc / 100)))
