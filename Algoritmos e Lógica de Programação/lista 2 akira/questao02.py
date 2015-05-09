'''
2. Determine se um ano é bissexto. Verifique no Google como fazer isso...
'''
print('Verificar se o ano é bissexto')
print()

ano = int(input('Digite o ano: '))
if len(str(ano)) == 4:
    if ano%4 == 0 and int(str(ano)[3:4]) != 00:
        bis = 'Foi bissexto'
    elif ano%4 == 0 and int(str(ano)[3:4]) == 00 and ano%400 == 0:
        bis = 'Foi bissexto'
    else:
        bis = 'Não foi bissexto'
    print('O ano de %d ele %s' %(ano,bis))
else:
    print('Favor digitar ano com 4 digitos')
