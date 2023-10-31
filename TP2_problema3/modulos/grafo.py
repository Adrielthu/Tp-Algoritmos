from TP2_problema3.modulos.vertice import Vertice
from TP2_problema3.modulos.monticulo_min import MonticuloBinarioTuplaMin
from TP2_problema3.modulos.monticulo_max import MonticuloBinarioTuplaMax

class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self,clave):
        """
        Esta funcion agrega un vertice a la clase Grafo

        Parametros
        ------------
        clave: TYPE: clave
                    Identifica el al vertice que se va a agregar

        Descripcion
        --------------
        Crea al Vertice y lo agraga al Grafo
   
        
        """
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

    def agregarArista(self, de, a, ponderacion=0, segunda_ponderacion=0):
                """
                Agrega arista entre dos vertices del grafo
                
                Parametros
                ------------
                de: TYPE: str
                        Clave del Vertice de origen
                a: TYPE: str
                        clave del Verice de destino
                Ponderacion: int
                Segunda_ponderacion: int
                
                Descripcion
                ------------
                Esta funcion agrega una arista del vertice de al vertice a                
                                
                """
                if de not in self.listaVertices:
                    nv = self.agregarVertice(de)
                if a not in self.listaVertices:
                    nv = self.agregarVertice(a)
                self.listaVertices[de].agregarVecino(self.listaVertices[a], ponderacion,segunda_ponderacion)

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())

    def __str__(self):
        result = ""
        for valor in self.listaVertices.values():
            result += f" {str(valor.id) } --> conectado a ---> { str([x for x in valor.conectadoA.keys()])}\n"
        return result

    def camino(self,unGrafo, salida, destino):
        """
        Esta funcion aplica los agloritmos dijkstra y dijstra_peso para
        encontrar el camino con mayor peso y su vez el menor precio

        Parametros
        -----------
        unGrafo: TYPE: grafo
        
        inicio: TYPE: vertice
        destino: TYPE: vertice
                    Indcican el vetice de destino y el vertice de salida
        
        
        
        """
        if salida in unGrafo.listaVertices and destino in unGrafo.listaVertices:
            grafo_peso = self.dijkstra_peso(unGrafo,salida, destino)
            distancias = []
        else:
            raise RuntimeError("Verifique la ciudad de inicio o de destino")
        if grafo_peso:
            for grafo in grafo_peso:
                grafo.dijkstra(grafo,salida)
                distancia_precio = grafo.obtenerVertice(destino).obtenerDistancia()
                distancias.append([grafo,distancia_precio])

            grafo_distancia = min(distancias, key=lambda x: x[1])

            distancia_precio = grafo_distancia[1]
            distancia_peso = self.listaVertices[destino].obtenerDistancia()

            camino = []
            actual = self.obtenerVertice(destino)
            while actual != None:
                camino.insert(0, actual)
                actual = actual.obtenerPredecesor()

            return camino, distancia_peso, distancia_precio
        else:
            return RuntimeError("No existe camino a ese destino")

    def dijkstra(self,unGrafo,inicio):
        """
        Esta funcion encuentra el precio minimo de vertice de inicio hacia todos
        los vertices del grafo

        Parametros
        -----------
        unGrafo: TYPE: Grafo

        inicio: TYPE: vertice
                    es el vertice de inicio del algoritmos dijkstra
        
        
        """
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
                            + verticeActual[1].obtenerSegundaPonderacion(verticeSiguiente)
                    if nuevaDistancia < verticeSiguiente.obtenerDistancia():
                        verticeSiguiente.asignarDistancia( nuevaDistancia )
                        verticeSiguiente.asignarPredecesor(verticeActual[1])
                        cp.decrementarClave(verticeSiguiente,nuevaDistancia)


    def dijkstra_peso(self, unGrafo, inicio, destino):
        """
        Esta funcion encuentra el maximo peso (cuello de botella) de un
        vertice de inicio hacia un vetice de destino

        Parametros
        -----------
        unGrafo: TYPE: Grafo

        inicio: TYPE: vertice
                    es el vertice de inicio del algoritmo
        destino: TYPE: vertice
                    vertice de llegada del algoritmo
        
        """
        cp = MonticuloBinarioTuplaMax()
        caminos = []
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

                        if verticeSiguiente.obtenerId() == destino:

                            nuevoGrafo = Grafo()
                            destino = self.obtenerVertice(destino)
                            while destino.obtenerPredecesor() is not None:
                                predecesor = destino.obtenerPredecesor()
                                ponderacion_primera = predecesor.obtenerPonderacion(destino)
                                ponderacion_segunda = predecesor.obtenerSegundaPonderacion(destino)
                                nuevoGrafo.agregarArista(predecesor.obtenerId(), destino.obtenerId(), ponderacion_primera, ponderacion_segunda)
                                destino = predecesor
                            caminos.append(nuevoGrafo)

        return caminos
