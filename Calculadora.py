n1 = input ("Por favor introduzca el primer numero: ")
n2 = input ("Por favor introduzca el segundo numero: ")
n1 = float (n1)
n2 = float (n2)
c1 = input ("Por favor introduzca la operacion a realizar. Suma (1), Resta (2), Division (3), Multiplicacion (4): ")

resultado = 0

if c1 == '1':
    resultado = n1 + n2
elif c1 == '2':
    resultado = n1 - n2
elif c1 == '3':
    resultado = n1 / n2
elif c1 == '4':
    resultado = n1 * n2
else:
    print ("La opcion ingreada es invalida")

print (resultado)