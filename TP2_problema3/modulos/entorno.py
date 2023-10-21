from TP2_problema3.modulos.grafo import Grafo
import matplotlib.pyplot as plt
import networkx as nx

class EntornoRutas():
    def __init__(self):
        self.grafo_peso = Grafo()
        self.grafo_precio = Grafo()

    def construir_grafo(self,archivo):
        with open(archivo,'r') as rutas:
            lectura = rutas.readlines()

            tabla = []
            for ruta in lectura:
                dato = ruta.strip().split(',')
                if dato[0] not in self.grafo_peso:
                    self.grafo_peso.agregarVertice(dato[0])
                    self.grafo_precio.agregarVertice(dato[0])
                tabla.append(dato)
        for fila in tabla:
            salida = fila[0]
            destino = fila[1]
            peso = int(fila[2])
            precio = int(fila[3])
            self.grafo_peso.agregarArista(salida,destino,peso)
            self.grafo_precio.agregarArista(salida,destino,precio)

    def numeroDeVertices(self):
        print(self.grafo_peso.numVertices)

    def mostrar_caminos(self):
        print(self.grafo_peso)

    def precio_min(self,inicio,destino):
        self.grafo_precio.dijkstra(self.grafo_precio,inicio)
        # print(self.grafo_precio.camino(inicio, destino))

        self.grafo_peso.dijkstra_peso(self.grafo_peso,inicio)
        # print(self.grafo_peso.camino(inicio, destino))

        resultado = f"Precio:\n{self.grafo_precio.camino(inicio, destino)}\n\nPeso:\n{self.grafo_peso.camino(inicio, destino)}"
        print(resultado)

    def graficar(self, usar_grafo_precio=True):
        if usar_grafo_precio:
            grafo = self.grafo_precio
        else:
            grafo = self.grafo_peso
        self._grafica(grafo)

    def _grafica(self,grafo):
        G = nx.DiGraph()

        for vertice in grafo.obtenerVertices():
            G.add_node(vertice)

        # Agrega aristas desde tu grafo personalizado
        for vertice in grafo:
            for vecino in vertice.obtenerConexiones():
                G.add_edge(vertice.obtenerId(), vecino.obtenerId(), weight=vertice.obtenerPonderacion(vecino))

        # Dibuja el gráfico
        pos = nx.spring_layout(G)
        labels = {n: n for n in G.nodes()}
        nx.draw(G, pos, with_labels=True, labels=labels, node_color='skyblue', font_weight='bold', node_size=100)

        # Dibuja etiquetas de ponderación en las aristas
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.show()
