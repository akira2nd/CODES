'''
5. Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras 
“python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para 
minúsculas e de remover antes os caracteres especiais.
'''
texto = 'The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'
texto1 = texto.replace('.','')
texto1 = texto1.replace(',','')
texto1 = texto1.lower()
texto1 = texto1.split()

cont = 0

for a in texto1:
    
    if len(a) > 4:
        
        for b in a:
            if b in 'phyton':
                'print(a)'
                cont += 1
                break

print('%d palavras contem uma das letras "phyton" e são maiores de 4 caracteres' %cont)
