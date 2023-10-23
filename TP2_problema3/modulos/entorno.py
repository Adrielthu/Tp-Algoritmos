from TP2_problema3.modulos.grafo import Grafo
import matplotlib.pyplot as plt
import networkx as nx


class ServicioDeTransporte:
    def __init__(self):
        self.grafo = Grafo()

    def construir_rutas(self, archivo):
        with open(archivo, "r") as rutas:
            lectura = rutas.readlines()

            tabla = []
            for ruta in lectura:
                dato = ruta.strip().split(",")
                if dato[0] not in self.grafo:
                    self.grafo.agregarVertice(dato[0])
                tabla.append(dato)
        for fila in tabla:
            salida = fila[0]
            destino = fila[1]
            peso = int(fila[2])
            precio = int(fila[3])
            self.grafo.agregarArista(salida, destino, peso, precio)

    def numeroDeCiudades(self):
        print(self.grafo.numVertices)

    def mostrar_caminos(self):
        print(self.grafo)

    def precio_min(self, inicio, destino):
        prueba = self.grafo.camino(self.grafo, inicio, destino)

        if isinstance(prueba, RuntimeError):
            print(f"Error: {prueba}")
        else:
            print(
                f"El camino de {inicio} a {destino} es\n{prueba[0]}\nEste es el peso\n{prueba[1]}\nY el precio\n{prueba[2]}"
            )

    def graficar(self):
        G = nx.DiGraph()
        for vertice in self.grafo.obtenerVertices():
            G.add_node(vertice)

        # Agrega aristas con dos atributos de ponderación
        for vertice in self.grafo:
            for vecino in vertice.obtenerConexiones():
                salida = vertice.obtenerId()
                destino = vecino.obtenerId()
                peso = vertice.obtenerPonderacion(vecino)
                precio = vertice.obtenerSegundaPonderacion(vecino)

                G.add_edge(salida, destino, peso=peso, precio=precio)

        # Dibuja el gráfico
        pos = nx.spring_layout(G)
        labels = {
            edge: (G.edges[edge]["peso"], G.edges[edge]["precio"]) for edge in G.edges
        }
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_color="skyblue",
            font_weight="bold",
            node_size=100,
        )
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        plt.show()
