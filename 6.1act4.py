
Cant_alumnos = int(input("Ingrese cantidad de alumnos que rindieron examen: "))
 
Suma_nota = 0

for i in range(Cant_alumnos):
    nota = int(input("Ingrese nota del alumno: "))
    Suma_nota += nota  #importante ver la expresion de esta variable acum
    promedio = Suma_nota / Cant_alumnos
    
if promedio > 8:
      print("El rendimiento es de",promedio,"elevado")
elif promedio >=6 and promedio <= 8: #VER el uso de "ELIF"!!!
      print("El rendimiento es de",promedio,"aceptable")
else:
     print("El rendimiento es de", promedio, "bajo")


