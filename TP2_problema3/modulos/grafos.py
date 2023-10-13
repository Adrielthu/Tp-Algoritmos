from TP2_problema3.modulos.abb import Grafo , Vertice
from TP2_problema1.modulos.monticulo import MonticuloBinario

class GrafoPeso(Grafo):
    def dijkstra(self,unGrafo,inicio):
        cp = MonticuloBinario()
        inicio.asignarDistancia(0)
        cp.construirMonticulo([(v.obtenerDistancia(),v) for v in unGrafo])
        while not cp.estaVacia():
            verticeActual = cp.eliminarMin()
            for verticeSiguiente in verticeActual.obtenerConexiones():
                nuevaDistancia = verticeActual.obtenerDistancia() \
                        + verticeActual.obtenerPonderacion(verticeSiguiente)
                if nuevaDistancia < verticeSiguiente.obtenerDistancia():
                    verticeSiguiente.asignarDistancia( nuevaDistancia )
                    verticeSiguiente.asignarPredecesor(verticeActual)
                    cp.decrementarClave(verticeSiguiente,nuevaDistancia)

class GrafoPrecio(Grafo):
    pass

