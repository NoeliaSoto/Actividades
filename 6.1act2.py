# Mostrar sólo los números pares desde 0 hasta el número ingresado (input). Nota: para saber si un número es par hacer i % 2 == 0)

numero = int(input("Ingrese un numero entero: "))

for i in range(numero+1): #sumo 1 porque supongo que es hasta el numero ingresado INCLUSIVE y python toma desde el cero
    if i % 2 == 0:
        print(i)
    
