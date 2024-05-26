#Corroborar si la clave fiscal de un cliente es "D0r1t@98" y coincide con la clave registrada en su estudio contable


clave_fiscal = input("Ingresar clave fiscal: ")
clave_registrada = input("ingresar clave registrada:")

if clave_fiscal == "D0r1t@98" and clave_fiscal == clave_registrada:
    print("El registro se encuentra actualizado")