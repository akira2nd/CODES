import urllib.request
import random

#sorteia a palavra e armazena na variavel
def sorteia():
    url = 'http://www.ime.usp.br/~pf/algoritmos/dicios/br'
    return urllib.request.urlopen(url).read().decode('iso8859').split()

#desenha a forca
def desenha(x):
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
    return forca[x]
        
#recebe as letras certas + erradas
def chute(letra):
    return

#pergunta se quer jogar de novo
def again():
    return '0' == input('\n\tJogo da Forca\n\n Digite "0"(zero) para jogar novamente: ')

lista = sorteia()

while True:
    certa = str()
    errado = str()
    n = 0
    palavra = lista[random.randint(0,len(lista))]
    nPalavra = '-'*len(palavra)
    while n < 8:
        print(desenha(n))
        print(nPalavra)
        print('letras certas:',certa)
        print('letras erradas:',errado)
        if n != 7:
            letra = input('Chute uma letra: ')
        else:
            break
        if letra.isalpha():
            if letra in palavra:
                certa += letra
                for l in range(len(palavra)):
                    if palavra[l] == letra:
                        nPalavra = nPalavra[:l] + letra + nPalavra[l+1:]
            
            else:
                errado += letra
                n += 1
        else:
            print('Caracter inválido digite novamente!')
            
        if nPalavra == palavra:
            print(desenha(n))
            print(nPalavra)
            print('Palavra certa Parabéns!!!')
            break
    if not again():
        break        

