#Lista: colección ordenada y modificable. Permite miembros duplicados
#Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas, guardarlos en una lista y mostrarlos
Nombres_personas = []

for i in range(10): # CONOZCO la cantidad > utilizo FOR
    nombre = input("Ingrese nombre de una persona: ")
    if nombre in Nombres_personas:
        print("El nombre", nombre, "ya fue ingresado, introduzca otro")
    else:
        Nombres_personas.append(nombre) #de esta forma agrego el nombre a la lista si es que no está repetido
print("Los 10 nombres ingresados son: ",Nombres_personas)

Nombres_personas.pop(2)
Nombres_personas.pop(-1)

print("La Nueva lista con la tercer y ultima persona eliminada es la siguiente", Nombres_personas)