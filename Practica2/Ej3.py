diccJuego= {}	#Creo el diccionario
for x in range(3): #Defino la estructura iterativa para ingresar 3 jugadores
	nombre = input("Ingrese nombre del jugador: ") #Leo la clave por teclado"""
	diccJuego[nombre] = {"Nivel": int(input("Ingrese nivel alcanzado en el juego: ")), "Puntaje": int(input("Ingrese puntaje máximo: ")), "Tiempo": float(input("Ingrese tiempo de juego: "))}
	print()
		#Para cada clave leida le asignamos un valor que será otro diccionario que va a contener los pares clave-valor
			#que referenciaran al dato que se almacena (clave) y al valor que va a adquirir (valor)"""

'''Comienzo ejercicio 3'''
lista = list(diccJuego.keys())

def top3():
	for i in range (0,3):
		aux = lista[i]
		print(aux + str(diccJuego[aux]))
		
def apellido():
	for valor in sorted(lista):
		print(valor + str(diccJuego[valor]))

def pjes():
	ranking = {}
	for nombre in diccJuego:
		if (diccJuego[nombre]['Puntaje'] in ranking):
			ranking[int([nombre['Puntaje']])+1] = nombre
		else:
			ranking[diccJuego[nombre]['Puntaje']] = nombre
	print (ranking)


'''
(a) Imprimir los 10 primeros puntajes de la estructura.
(b) Imprimir los datos de los usuarios ordenados alfabéticamente por apellido.
(c) Imprimir los datos de los usuarios ordenados por nivel alcanzado.
4. Imprima un listado de los archivos que contiene el directorio actual. La informa '''

top3()
print()
apellido()
print()
pjes()
