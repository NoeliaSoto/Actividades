#Diccionario: una colección ordenada, modificable y que no permite duplicados

nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
dni = int(input("Ingrese el DNI: "))
email = input("Ingrese el email: ")
fecha_nacimiento = input("Ingrese la fecha de nacimiento")

dicc_persona = {
    "nombre": nombre,
    "apellido": apellido,
    "dni": dni,
    "email": email,
    "fecha_nacimiento": fecha_nacimiento
}
print(dicc_persona)