from TP2_problema3.modulos.abb import Grafo

with open('rutas.txt','r') as rutas:
    lectura = rutas.readlines()

    tabla = []
    
    grafo_peso = Grafo()
    for ruta in lectura:
        dato = ruta.strip().split(',')
        grafo_peso.agregarVertice(dato[0])
        tabla.append(dato)

    print(grafo_peso.numVertices)


for fila in tabla:
    salida = fila[0]
    destino = fila[1]
    peso = int(fila[2])
    grafo_peso.agregarArista(salida,destino,peso)

print (grafo_peso)
    

