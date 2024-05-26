precio_neto= float(input("Ingrese el precio neto: "))
IVA = float(input("Ingrese alicuota de IVA: "))
Precio_total = precio_neto * (1 + IVA)

print("El precio total es", Precio_total)