#3) Escreva um programa que leia a quantidade de
#   dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
print('Converter dias, horas, minutos e segundo em segundos')
print()

d = int(input('Digite um valor inteiro para dias: '))
h = int(input('Digite um valor inteiro para horas: '))
m = int(input('Digite um valor inteiro para minutos: '))
s = int(input('Digite um valor inteiro para segundos: '))

ds = (d * 86400) + (h * 3600) + (m * 60) + s

print('%ddias, %02dh%02dm%02ds é igual a %d segundos' %(d,h,m,s,ds))
