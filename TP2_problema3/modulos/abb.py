# -*- coding: utf-8 -*-
from TP2_problema3.modulos.vertice import Vertice
from TP2_problema3.modulos.monticulo_tupla import MonticuloBinarioTupla
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
        for vertice, conexiones in self.listaVertices.items():
            result += f" {conexiones}\n"
        return result

    def camino(self,salida, destino):
        camino = []
        actual = destino
        while actual != None:
            camino.insert(0, actual)
            actual = self.listaVertices[actual].predecesor
        return [camino, self.listaVertices[destino].distancia]
    
    def dijkstra(self,unGrafo,inicio):
        cp = MonticuloBinarioTupla()
        if inicio in self.listaVertices:
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
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
