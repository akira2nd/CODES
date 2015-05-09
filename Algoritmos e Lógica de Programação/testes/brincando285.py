mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

m = input('Digite uma data DD/MM/AAA : ')
m = m.split('/')
x = int(m[1])
x -= 1

print('você digitou dia %s de %s de %s' %(m[0],mes[x],m[2]))
