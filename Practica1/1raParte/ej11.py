#Creo el diccionario

diccJuego= {}

#Cargo datos (en forma de diccionario) predefinidos en el diccionario 

diccJuego["Juan"] = {"Nivel": 12, "Puntaje": 124, "Tiempo": 1.5}
diccJuego["Diego"] = {"Nivel": 22, "Puntaje": 9, "Tiempo": 122.5}
diccJuego["Pedro"] = {"Nivel": 32, "Puntaje": 114, "Tiempo": 15.5}

#Imprimo el diccionario línea a línea

for key in diccJuego:
  print (key, ":", diccJuego[key])
print()

#Leo la clave por teclado (el nuevo nombre)

nombre = input("Ingrese nombre del jugador: ")

#Creo un diccionario auxiliar con los datos del nuevo nombre que leo desde teclado

aux = {"Nivel": int(input("Ingrese nivel alcanzado en el juego: ")), "Puntaje": int(input("Ingrese puntaje máximo: ")), "Tiempo": float(input("Ingrese tiempo de juego: "))}

"""
#Si la clave no está en el diccionario original, la agrego (con su respectivo valor)
if nombre not in diccJuego:
	diccJuego[nombre] = aux
	
#Si la clave está en el diccionario original, actualizo el puntaje nuevo (en caso de ser mayor que el anterior)
elif aux["Puntaje"] > diccJuego[nombre]["Puntaje"]:
	diccJuego[nombre] = aux
print()
"""

if (nombre not in diccJuego) or (aux["Puntaje"] > diccJuego[nombre]["Puntaje"]):
	diccJuego[nombre] = aux

#Imprimo el diccionario
for key in diccJuego:
  print (key, ":", diccJuego[key])
			
#Imprimir 10 mejores pjes

#Creo un nuevo diccionario que contendrá el ranking de los mejores puntajes
diccRanking = {}

#Itero por todo el diccionario original volcando los pares clave:valor (Puntaje:nombre) en el nuevo diccionario
for x in diccJuego:
	diccRanking[diccJuego[x]["Puntaje"]] = x
	
#Ordeno el diccionario del ranking con clave descendente
l = sorted(diccRanking, reverse=True)
print(l)

#Hago variables para mostrar los 3 puntajes más altos
inicio = 0
final = 3

#Imprimo los puntajes más altos
print("Los puntajes más altos fueron: ")
print()
if inicio != final:
	for pje in l:
		print("#", inicio+1, diccRanking[pje], pje)
		inicio = inicio + 1
		if inicio == final:
			break

