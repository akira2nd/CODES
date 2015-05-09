'''
2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao 
nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''
while True:
    usuário = input('Digite um usuário: ')
    senha = input('Digite uma senha: ')

    if usuário == senha:
        print('senha deve ser diferente do nome de usuário!')
    else:
        break

print('Usuário e senha OK')
