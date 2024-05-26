#Entrada de datos: nota_1, nota_2, nota_3, nota_4 y nota_5
#Tipo de datos: números enteros
#Proceso: se solicita al usuario que ingrese las notas, para luego calcular el promedio de las mismas
#Salida: Promedio de las notas ingresadas.
nota_1 = int(input("Ingrese la primera nota: "))
nota_2 = int(input("Ingrese la segunda nota: "))
nota_3 = int(input("Ingrese la tercera nota: "))
nota_4 = int(input("Ingrese la cuarta nota: "))
nota_5 = int(input("Ingrese la quinta nota: "))

suma = nota_1 + nota_2 + nota_3 + nota_4 + nota_5
promedio = suma / 5

print("El promedio de las 5 notas es",promedio)