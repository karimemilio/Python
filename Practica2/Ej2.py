'''Importo la funcion random'''
import random

'''Defino las estructuras a usar'''
colores = ['azul','amarillo','rojo','blanco','negro']
coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]

'''Defino funciones del ejercicio 2'''
def sumar():
	a = random.randrange(10)
	b = random.randrange(10)
	res = input('La suma de ' + str(a) + ' y ' + str(b) + ' es:')
	if (int(res) == (a+b)):
		print('Correcto')
	else:
		print('Incorrecto')
		
def palabra():
	palabras = [('grave',['molesto']), ('aguda',['ratón']),('esdrujula',['murciélago'])]
	aux = random.choice(palabras)
	res = input('La palabra '+ ''.join(aux[1]) + ' es: \n1. Grave\n2. Aguda\n3. Esdrujula\n')
	if int(res) == 1:
		sol = 'grave'
	elif int(res) == 2:
		sol = 'aguda'
	else:
		sol = 'esdrujula' 
	if (sol == aux[0]):
		print('Correcto')
	else:
		print('Incorrecto')

'''Defino y creo el diccionario del punto 1'''
dicc1 = {}
for coor in coordenadas:
	dicc1[coor] = random.choice(colores)

'''Imprimir resultado del punto 1'''
print('Estructura con repeticiones de colores:')
print(dicc1)
print()

'''Defino y creo el diccionario del punto 2'''
dicc2 = {}
for coor in coordenadas:
	dicc2[coor] = random.choice(colores)
	colores.remove(dicc2[coor])

'''Imprimir resultado del punto 2'''
print('Estructura sin repeticiones de colores:')
print(dicc2)
print()

'''COMIENZO DEL EJERCICIO 2'''
funciones = [sumar, palabra]
diccFunciones = {'azul': random.choice(funciones),
				'amarillo': random.choice(funciones),
				'rojo': random.choice(funciones),
				'blanco': random.choice(funciones),
				'negro': random.choice(funciones)}
tup = (int(input('Ingrese una coordenada X: ')), int(input('Ingrese una coordenada Y: ')))
if (tup in coordenadas):
	diccFunciones[dicc2[tup]]()
	'''Recibo el nombre de la funcion y la invoco con parentesis'''
else:
	print('No es una coordenada valida')
