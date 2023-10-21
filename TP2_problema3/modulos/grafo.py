from TP2_problema3.modulos.vertice import Vertice
from TP2_problema3.modulos.monticulo_min import MonticuloBinarioTuplaMin
from TP2_problema3.modulos.monticulo_max import MonticuloBinarioTuplaMax

class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self,clave):
        if clave not in self.listaVertices:
            self.numVertices = self.numVertices + 1
            nuevoVertice = Vertice(clave)
            self.listaVertices[clave] = nuevoVertice
            return nuevoVertice

    def obtenerVertice(self,n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.listaVertices

    def agregarArista(self,de,a,costo=0):
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        if a not in self.listaVertices:
            nv = self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())

    def __str__(self):
        result = ""
        for valor in self.listaVertices.values():
            result += f" {str(valor.id) } --> conectado a ---> { str([x for x in valor.conectadoA.keys()])}\n"
        return result

    def camino(self,salida, destino):
        camino = []
        actual = self.obtenerVertice(destino)
        while actual != None:
            camino.insert(0, actual)
            actual = actual.obtenerPredecesor()
        return [camino, self.listaVertices[destino].obtenerDistancia()]

    def dijkstra(self,unGrafo,inicio):
        for v in unGrafo:
             v.asignarDistancia(float('inf'))

        cp = MonticuloBinarioTuplaMin()
        if inicio in self.listaVertices:
            inicio = self.obtenerVertice(inicio)
            inicio.asignarDistancia(0)
            cp.construirMonticulo([(v.obtenerDistancia(),v) for v in unGrafo])
            while not cp.estaVacia():
                verticeActual = cp.eliminarMin()
                for verticeSiguiente in verticeActual[1].obtenerConexiones():
                    nuevaDistancia = verticeActual[1].obtenerDistancia() \
                            + verticeActual[1].obtenerPonderacion(verticeSiguiente)
                    if nuevaDistancia < verticeSiguiente.obtenerDistancia():
                        verticeSiguiente.asignarDistancia( nuevaDistancia )
                        verticeSiguiente.asignarPredecesor(verticeActual[1])
                        cp.decrementarClave(verticeSiguiente,nuevaDistancia)


    def dijkstra_peso(self, unGrafo, inicio):
        cp = MonticuloBinarioTuplaMax()

        if inicio in self.listaVertices:
            inicio = self.obtenerVertice(inicio)
            inicio.asignarDistancia(float('inf'))
            cp.construirMonticulo([(v.obtenerDistancia(), v) for v in unGrafo])

            while not cp.estaVacia():
                verticeActual = cp.eliminarMax()

                for verticeSiguiente in verticeActual[1].obtenerConexiones():
                    nuevaDistancia = min(verticeActual[1].obtenerDistancia(),
                                        verticeActual[1].obtenerPonderacion(verticeSiguiente))

                    if nuevaDistancia > verticeSiguiente.obtenerDistancia():
                        verticeSiguiente.asignarDistancia(nuevaDistancia)
                        verticeSiguiente.asignarPredecesor(verticeActual[1])
                        cp.decrementarClave(verticeSiguiente, nuevaDistancia)