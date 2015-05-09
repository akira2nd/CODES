'''
Questão D. Daniela é uma pessoa muito supersticiosa. Para ela, um número é sortudo 
se ele contém o dígito 2 mas não o dígito 7. Então, na opinião dela, quantos números 
sortudos existem entre 18644 e 33087, incluindo os extremos?
Resposta: 7995
'''
x = 18644
cont = 0
while x <= 33087:
    if str(2) in str(x) and str(7) not in str(x):
        cont += 1
    x += 1

print(cont)
