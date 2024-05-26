#Situacion 1: Verificar si hay saldo suficiente para comprar un pasaje

Importe_pasaje = float(input("Ingrese valor del pasaje: "))

Saldo_Cuenta = float(input("Ingrese saldo actual de la cuenta: "))

if Importe_pasaje <= Saldo_Cuenta:
    print("Saldo suficiente, el valor de la compra es", Importe_pasaje)

