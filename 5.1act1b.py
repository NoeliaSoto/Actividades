#Verificar si la declaracion de un cliente arroja IVA a pagar o si posee un saldo a favor trasladable

Debito_Fiscal = float(input("Ingrese débito fiscal computable: "))
Credito_Fiscal = float(input("Ingrese crédito fiscal computable: "))

if Debito_Fiscal > Credito_Fiscal:
    print("El cliente deberá pagar IVA")
else:
    print("Posee un saldo a favor trasladable al siguiente periodo")