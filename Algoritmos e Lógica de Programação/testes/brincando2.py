#considere a empresa de telefonia Tchau.
#Abaixo de 200 minutos, a empresa cobra R$0,20 por minuto.
#Entre 200 e 400 minutos, o preço é R$0,18.
#Acima de 400 minutos o preço por minuto é R$0,15.
#Calcule sua conta de telefone

#t <= 200 = t * 0.20
#t >= 201 and t <= 400 = t * 0.18

t = int(input("Quantos minutos você usou o telefone? : "))

if t <= 200:
    print("Você vai pargar R$%.2f na conta da empresa Tchau" %(t*0.20))
else:
    if t >= 201 and t <= 400:
        print("Você vai pargar R$%.2f na conta da empresa Tchau" %(t*0.18))
    else:
        print("Você vai pargar R$%.2f na conta da empresa Tchau" %(t*0.15))

