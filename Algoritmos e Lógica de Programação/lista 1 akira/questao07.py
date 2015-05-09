#7) Converta uma temperatura digitada em Celsius para Fahrenheit.
#   F = 9*C/5 + 32
print('Converter temperatura Celsius(ºC) para Fahrenheit(ºF)')
print()

tempC = float(input('Digite a temperatura em graus Celsius: '))

fahr = 9* tempC /5+32

print('A temperatura convertida em Fahrenheit é de %.2f°F' % fahr)
