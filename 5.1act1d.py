#Determinar si un cliente posee deudas impositivas o bancarias en el balance contable

Deuda_Impositivas = float(input("Ingrese importe de las deudas impositivas: "))
Deuda_Bancaria = float(input("Ingrese importe de deudas bancarias: "))

if Deuda_Impositivas > 0 or Deuda_Bancaria > 0:
    print("Posee deudas")
else:
    print("No posee deudas")