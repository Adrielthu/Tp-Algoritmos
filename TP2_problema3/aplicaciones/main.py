from TP2_problema3.modulos.abb import Grafo
import matplotlib.pyplot as plt
import networkx as nx
with open('rutas.txt','r') as rutas:
    lectura = rutas.readlines()

    tabla = []

    grafo_peso = Grafo()
    for ruta in lectura:
        dato = ruta.strip().split(',')
        if dato[0] not in grafo_peso:
            grafo_peso.agregarVertice(dato[0])
        tabla.append(dato)

    print(grafo_peso.numVertices)


for fila in tabla:
    salida = fila[0]
    destino = fila[1]
    peso = int(fila[2])
    grafo_peso.agregarArista(salida,destino,peso)

print (grafo_peso)

G = nx.Graph()

for vertice in grafo_peso.obtenerVertices():
    G.add_node(vertice)

# Agrega aristas desde tu grafo personalizado
for vertice in grafo_peso:
    for vecino in vertice.obtenerConexiones():
        G.add_edge(vertice.obtenerId(), vecino.obtenerId(), weight=vertice.obtenerPonderacion(vecino))

# Dibuja el gráfico
pos = nx.spring_layout(G)  # Esto es para calcular las posiciones de los nodos
labels = {n: n for n in G.nodes()}  # Etiquetas de nodos
nx.draw(G, pos, with_labels=True, labels=labels, node_color='skyblue', font_weight='bold', node_size=100)

# Dibuja etiquetas de ponderación en las aristas
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()