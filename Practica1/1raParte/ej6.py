frase = "Si trabajás mucho con computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en ungran número de archivos de texto, o renombrar y reorganizar un montón de archivos con fotosde una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada,o una aplicación especializada con interfaz gráfica, o un juego simple."
lista = frase.upper().split(' ')
print(lista)
dicc = {}
for x in lista:
	if len(x) in dicc:
		dicc[len(x)].append(x)
	else:
		dicc[len(x)] = [x]
print("")
print("")
print("")
print(dicc)
