diccJuego= {}	#Creo el diccionario
for x in range(3): #Defino la estructura iterativa para ingresar 3 jugadores
	nombre = input("Ingrese nombre del jugador: ") #Leo la clave por teclado"""
	diccJuego[nombre] = {"Nivel": int(input("Ingrese nivel alcanzado en el juego: ")), "Puntaje": int(input("Ingrese puntaje máximo: ")), "Tiempo": float(input("Ingrese tiempo de juego: "))}
	print()
		#Para cada clave leida le asignamos un valor que será otro diccionario que va a contener los pares clave-valor
			#que referenciaran al dato que se almacena (clave) y al valor que va a adquirir (valor)"""
imp = input("Ingrese el nombre de un Usuario a buscar: ")
if imp in diccJuego:
		print(diccJuego[imp])
else:
	print("No se encuentra el nombre de Usuario")
