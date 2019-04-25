'''Importo la funcion random'''
import random

'''Defino las estructuras a usar'''
colores = ['azul','amarillo','rojo','blanco','negro']
coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]

'''Defino y creo el diccionario del ejercicio 1'''
dicc1 = {}
for coor in coordenadas:
	dicc1[coor] = random.choice(colores)

'''Imprimir resultado del ejercicio 1'''
print('Estructura con repeticiones de colores:')
print(dicc1)
print()

'''Defino y creo el diccionario del ejercicio 2'''
dicc2 = {}
for coor in coordenadas:
	dicc2[coor] = random.choice(colores)
	colores.remove(dicc2[coor])

'''Imprimir resultado del ejercicio 2'''
print('Estructura sin repeticiones de colores:')
print(dicc2)
print()

"""Generar una estructura que contenga coordenadas y un color asociado. La forma de
asociar las coordenadas con el color debe ser aleatoria sin importar que se repitan los
colores elegidos.

Generar una estructura que contenga coordenadas y un color asociado. La forma de
asociar las coordenadas con el color debe ser aleatoria sin que se repitan los colores"""
