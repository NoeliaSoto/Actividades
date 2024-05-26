Partidos_perdidos= int(input("Ingrese la cantidad de partidos perdidos : "))
Partidos_empatados= int(input("Ingrese la cantidad de partidos empatados: "))
Partidos_ganados= int(input("Ingrese la cantidad de partidos ganados : "))

Puntaje_Partidos = Partidos_perdidos * 0 + Partidos_empatados * 1 + Partidos_ganados * 3


print("La cantidad de puntos del equipo es de",Puntaje_Partidos)