Algoritmo act5
	Escribir "Ingrese valor del pasaje: "
    Leer Importe_pasaje
    
    Escribir "Ingrese saldo actual de la cuenta: "
    Leer Saldo_Cuenta
	
    SI Importe_pasaje <= Saldo_Cuenta Entonces
		Escribir "Saldo suficiente, el valor de la compra es ", Importe_pasaje
	FINSI
FinAlgoritmo
