#Ejercicio 13#
imagenes = ['im1','im2','im3']
dicc = {}
for x in imagenes:
	dicc[x] = set()
	print("Para la imagen " + x)
	cont = len(dicc[x])
	while len(dicc[x]) != 3:
		x1 = int(input("Ingrese la coordenada X" + str(cont + 1) + ": "))
		y1 = int(input("Ingrese la coordenada Y" + str(cont + 1) + ": "))
		print()
		tup = x1, y1
		dicc[x].add(tup)
		cont = len(dicc[x])
print (dicc)

#Ejercicio 14#

#tam={'im1':[(x_1,y_1),(x_2,y_2)],'im2':[(x_1,y_1),(x_2,y_2)],'im3':[(x_1,y_1),(x_2,y_2)]}#

tam={'im1':[(1,2),(3,3)],'im2':[(2,4),(2,2)],'im3':[(1,2),(4,9)]}

for imagen in dicc:
	for coordenada in dicc[imagen]:
		if (coordenada[0] >= tam[imagen][0][0]) and (coordenada[0] <= tam[imagen][1][0]) and (coordenada[1] >= tam[imagen][0][1]) and (coordenada[1] <= tam[imagen][1][1]):
			print("Ok")
		else:
			print("No ok")
