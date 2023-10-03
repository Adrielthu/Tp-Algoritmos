class NodoArbol:
    def __init__(self,clave, valor, padre=None, izquierdo=None, derecho=None):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoDerecho = derecho
        self.hijoIzquierdo = izquierdo
        self.padre = padre
        self.factorEquilibrio = 0
    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        return not self.padre

    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        return not self.padre
    
class AVL():
    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def agregar(self,clave,valor):
        if self.raiz:
            self._agregar(clave,valor,self.raiz)
        else:
            self.raiz = NodoArbol(clave,valor)
        self.tamano = self.tamano + 1

    def _agregar(self,clave,valor,nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                    self._agregar(clave,valor,nodoActual.hijoIzquierdo)
            else:
                    nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre=nodoActual)
                    self.actualizarEquilibrio(nodoActual.hijoIzquierdo)
        else:
            if nodoActual.tieneHijoDerecho():
                    self._agregar(clave,valor,nodoActual.hijoDerecho)
            else:
                    nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual)
                    self.actualizarEquilibrio(nodoActual.hijoDerecho)

    def actualizarEquilibrio(self,nodo):
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre != None:
            if nodo.esHijoIzquierdo():
                    nodo.padre.factorEquilibrio += 1
            elif nodo.esHijoDerecho():
                    nodo.padre.factorEquilibrio -= 1

            if nodo.padre.factorEquilibrio != 0:
                    self.actualizarEquilibrio(nodo.padre)

    def rotarIzquierda(self,rotRaiz):
        # La nueva raiz va a ser el hijo derecho de la raiz actual
        nuevaRaiz = rotRaiz.hijoDerecho
        # Si la nueva raiz tiene hijo izquierdo, ese va a ser el hijo derecho de la raiz que rota
        rotRaiz.hijoDerecho = nuevaRaiz.hijoIzquierdo
        # Esta condición es por si la nueva raiz tiene un hijo izquierdo
        if nuevaRaiz.hijoIzquierdo != None:
            # Se asigna el nuevo padre al hijo izquierdo
            nuevaRaiz.hijoIzquierdo.padre = rotRaiz
        # La nueva raiz ahora apunta al padre de la antigua raiz
        nuevaRaiz.padre = rotRaiz.padre
        # Si la anterior raiz es self.raiz, ahora nueva raiz va a ser self.raiz
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            # En el caso de que no se cumpla lo anterior
            # hay que ver si la anterior raiz es un hijo izquierdo
            # para que ahora el nuevo hijo izquierdo sea la nueva raiz
            if rotRaiz.esHijoIzquierdo():
                    rotRaiz.padre.hijoIzquierdo = nuevaRaiz
            # Si no, el nuevo hijo derecho va a ser la nueva raiz
            else:
                rotRaiz.padre.hijoDerecho = nuevaRaiz
        # La antigua raiz ahora es el hijo izquierdo de la nueva raiz
        nuevaRaiz.hijoIzquierdo = rotRaiz
        # Se actualiza el padre de la antigua raiz
        rotRaiz.padre = nuevaRaiz
        # Se actualiza el factor de equilibrio
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio + 1 + max(rotRaiz.factorEquilibrio, 0)

    def rotarDerecha(self,rotRaiz):
        nuevaRaiz = rotRaiz.hijoIzquierdo
        rotRaiz.hijoIzquierdo = nuevaRaiz.hijoDerecho
        if nuevaRaiz.hijoDerecho != None:
            nuevaRaiz.hijoDerecho.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoIzquierdo():
                rotRaiz.padre.hijoIzquierdo = nuevaRaiz
            else:
                rotRaiz.padre.hijoDerecho = nuevaRaiz
        nuevaRaiz.hijoDerecho = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio += (-1 - max(nuevaRaiz.factorEquilibrio, 0))
        nuevaRaiz.factorEquilibrio += (-1 - max(rotRaiz.factorEquilibrio, 0))

    def reequilibrar(self,nodo):
        if nodo.factorEquilibrio < 0:
                if nodo.hijoDerecho.factorEquilibrio > 0:
                    self.rotarDerecha(nodo.hijoDerecho)
                    self.rotarIzquierda(nodo)
                else:
                    self.rotarIzquierda(nodo)
        elif nodo.factorEquilibrio > 0:
                if nodo.hijoIzquierdo.factorEquilibrio < 0:
                    self.rotarIzquierda(nodo.hijoIzquierdo)
                    self.rotarDerecha(nodo)
                else:
                    self.rotarDerecha(nodo)

    def inorden(self, nodo):
        if nodo:
            self.inorden(nodo.hijoIzquierdo)
            print(nodo.clave, end=" ")
<<<<<<< HEAD
            self.inorden(nodo.hijoDerecho)


    

arbol = AVL()

raiz = None
claves = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
    
for clave in claves:
    raiz = arbol.agregar(clave, raiz)

print(arbol.inorden(arbol.raiz))
=======
            self.inorden(nodo.derecha)
>>>>>>> 316424d6faef09a7a70f1774781eff5461a62e7b
