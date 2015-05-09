print ("Lembre-se, octal vai de 0 a 7, binário 0 e 1, hexa de 0 a F")
base = int(input("Base: "))
num = str(input("Número: "))
resultado = 0
n = len(num)-1
for x in num:
     if x in "0123456789":
          x = int(x)
     if x == "A" or x == "a":
          x = 10
     elif x == "B" or x == "b":
          x = 11
     elif x == "C" or x == "c":
          x = 12
     elif x == "D" or x == "d":
          x = 13
     elif x == "E" or x == "e":
          x = 14
     elif x == "F" or x == "f":
          x = 15
     z = x * base ** n
     print("%d x %d ** %d = %d" %(x, base, n, z))
     n -= 1
     resultado += z
print("Resultado em decimal: %d" %resultado)
