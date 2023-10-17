
class Vertice:
    def __init__(self,clave):
        self.id = clave
        self.conectadoA = {}
        self.distancia = float('inf')
        self.predecesor = None
        self.visitado = False
        self.color = 'Blanco'

    def agregarVecino(self,vecino,ponderacion=0):
        self.conectadoA[vecino] = ponderacion

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return self.__str__()

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerId(self):
        return self.id

    def obtenerPonderacion(self,vecino):
        return self.conectadoA[vecino]

    def asignarPredecesor(self,predecesor):
        self.predecesor = predecesor

    def obtenerPredecesor(self):
        return self.predecesor

    def asignarDistancia(self, distancia):
        self.distancia = distancia

    def obtenerDistancia(self):
        return self.distancia

    def recorrer(y):
        x = y
        while (x.obtenerPredecesor()):
            print(x.obtenerId())
            x = x.obtenerPredecesor()
        print(x.obtenerId())

