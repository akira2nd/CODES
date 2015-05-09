def convert(numeroDecimal,base):
    a = int(numeroDecimal)
    b = int(base)
    resultado = ''
    while a != 0:
        inteiro =  int(a / b)
        resto = a % b
        if resto == 10:
            resto = 'A'
        elif resto == 11:
            resto = 'B'
        elif resto == 12:
            resto = 'C'
        elif resto == 13:
            resto = 'D'
        elif resto == 14:
            resto = 'E'
        elif resto == 15:
            resto = 'F'
        resultado += str(resto)
        print ("%d / %d = %d e resto: %s" %(a,b,inteiro,resto))
        a = int(a/b)
    return ("Resultado = %s" %(resultado[ : : -1]))
