#Mostrar los números desde el 0 al número solicitado al usuario (input)

numero = int(input("Ingrese un numero entero: "))

for i in range(numero + 1): #Si quiero que salga el numero que pide el cliente le debo sumar 1 porque python toma desde el CERO!!
    print(i)
