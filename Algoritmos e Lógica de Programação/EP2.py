import urllib.request
import random

def sorteia():
    url = 'http://www.ime.usp.br/~pf/algoritmos/dicios/br'
    return urllib.request.urlopen(url).read().decode('iso8859').split()

forca =['''
     +-----+
     |     |
           |
           |
           |
           |
============

''','''
     +-----+
     |     |
     o     |
           |
           |
           |
============

''','''
     +-----+
     |     |
     o     |
     |     |
           |
           |
============

''','''
     +-----+
     |     |
     o     |
     |     |
    /      |
           |
============

''','''
     +-----+
     |     |
     o     |
     |     |
    / \    |
           |
============

''','''
     +-----+
     |     |
     o     |
    /|     |
    / \    |
           |
============
''','''
     +-----+
     |     |
     o     |
    /|\    |
    / \    |
           |
============

''','''
     +-----+
     |     |
     o     |
    /|\    |
    / \    |
VOCÊ PERDEU|
============

''']

certa = str()
errada = str()

lista = sorteia()

c = 0
palavra = lista[random.randint(0,len(lista))]
oPalavra = '-' * len(palavra)
while len(palavra) > c:
    print(forca[c])
    print(oPalavra)
    print('certa:', certa)
    print('errado:',errada)
    letra = input('Digite a letra:')
    while True:
        if letra in certa or letra in errada:
            print('Letra já utilizada, digite novamente')
            break
        elif letra in palavra:
            certa = certa + letra
            for l in range(len(palavra)):
                if palavra[l] == letra:
                    oPalavra = oPalavra[:l-1] + letra + oPalavra[l:]
        else:
            errada += letra
            c = c + 1
        break

                        
    
        
    
