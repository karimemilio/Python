imagenes = ['im1','im2','im3']
dicc = {}
for x in imagenes:
	dicc[x] = set()
	print("Para la imagen " + x)
	cont = 1
	while len(dicc[x]) != 3:
		x1 = input("Ingrese la coordenada X" + str(cont) + ": ")
		y1 = input("Ingrese la coordenada Y" + str(cont) + ": ")
		print()
		tup = x1, y1
		dicc[x].add(tup)
		cont = len(dicc[x])
print (dicc)
