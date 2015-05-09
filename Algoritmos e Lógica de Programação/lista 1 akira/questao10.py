#10) Escreva um programa para calcular a redução do tempo de vida de um fumante.
#   Pergunte a quantidade de cigarros fumados por dia
#   e quantos anos ele já fumou.
#   Considere que um fumante perde 10 minutos de vida a cada cigarro,
#   calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

print('Extimativa de dias de vida perdidos de um fumante')
print()

cigarros = int(input('Quantos cigarros você fuma por dia? :'))
anos = int(input('Quantos anos você ja fumou? :'))

tempo = ((cigarros*10)/(24*60)) + (anos * 365)

print('Você perdeu cerca de %d dias de vida com o cigarro.' %tempo)
