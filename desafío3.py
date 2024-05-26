Importe_pesos = float(input("Ingrese importe en pesos (ARS): "))
Valor_cambio = float(input("Ingrese el valor del tipo de cambio actual (USD): "))
Importe_dólares = Importe_pesos / Valor_cambio

print("El importe total en dólares es", Importe_dólares)