# --------------------------------------------------------------------------------------------------------------
from nodoArbol import NodoArbol
# --------------------------------------------------------------------------------------------------------------

class AVL:
    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def agregar(self, clave, valor):
        if self.raiz:
            self._agregar(clave, valor, self.raiz)
        else:
            self.raiz = NodoArbol(clave, valor)
        self.tamano = self.tamano + 1

    def _agregar(self, clave, valor, nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                self._agregar(clave, valor, nodoActual.hijoIzquierdo)
            else:
                nodoActual.hijoIzquierdo = NodoArbol(clave, valor, padre=nodoActual)
                self.actualizarEquilibrio(nodoActual.hijoIzquierdo)
        else:
            if nodoActual.tieneHijoDerecho():
                self._agregar(clave, valor, nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = NodoArbol(clave, valor, padre=nodoActual)
                self.actualizarEquilibrio(nodoActual.hijoDerecho)

    def actualizarEquilibrio(self, nodo):
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

    def _actualizarEquilibrioEliminar(self, nodoAEliminar):
        if nodoAEliminar.esHijoIzquierdo():
            nodoAEliminar.padre.factorEquilibrio -= 1
        elif nodoAEliminar.esHijoDerecho():
            nodoAEliminar.padre.factorEquilibrio += 1
        if nodoAEliminar.padre != None:
            self._actualizarEquilibrioEliminar(nodoAEliminar.padre)

    def rotarIzquierda(self, rotRaiz):
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
        rotRaiz.factorEquilibrio = (
            rotRaiz.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio, 0)
        )
        nuevaRaiz.factorEquilibrio = (
            nuevaRaiz.factorEquilibrio + 1 + max(rotRaiz.factorEquilibrio, 0)
        )

    def rotarDerecha(self, rotRaiz):
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
        rotRaiz.factorEquilibrio = (
            rotRaiz.factorEquilibrio - 1 - max(nuevaRaiz.factorEquilibrio, 0)
        )
        nuevaRaiz.factorEquilibrio = (
            nuevaRaiz.factorEquilibrio - 1 + min(rotRaiz.factorEquilibrio, 0)
        )

    def reequilibrar(self, nodo):
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

    def __iter__(self):
        return self.inorden_iter(self.raiz)

    def inorden_iter(self, nodo):
        if nodo:
            yield from self.inorden_iter(nodo.hijoIzquierdo)
            yield nodo.clave
            yield from self.inorden_iter(nodo.hijoDerecho)

    def obtener(self, clave):
        if self.raiz:
            res = self._obtener(clave, self.raiz)
            if res:
                return res.cargaUtil
            else:
                return None
        else:
            return None

    def _obtener(self, clave, nodoActual):
        if not nodoActual:
            return None
        elif nodoActual.clave == clave:
            return nodoActual
        elif clave < nodoActual.clave:
            return self._obtener(clave, nodoActual.hijoIzquierdo)
        else:
            return self._obtener(clave, nodoActual.hijoDerecho)

    def eliminar(self, clave):
        if self.tamano > 1:
            # Busca el nodo a eliminar en el árbol
            nodoAEliminar = self._obtener(clave, self.raiz)
            if nodoAEliminar:
                # Obtiene el padre del nodo a eliminar
                padreNodoAEliminar = nodoAEliminar.padre

                # Actualiza el equilibrio del árbol después de eliminar el nodo
                self._actualizarEquilibrioEliminar(nodoAEliminar)

                # Realiza la eliminación del nodo
                self.remover(nodoAEliminar)

                # Verifica si el equilibrio del árbol se ha desviado
                if padreNodoAEliminar.factorEquilibrio > 1 or padreNodoAEliminar.factorEquilibrio < -1:
                    # Reequilibra el árbol a partir del padre del nodo eliminado
                    self.reequilibrar(padreNodoAEliminar)

                self.tamano = self.tamano - 1
            else:
                raise KeyError("Error, la clave no está en el árbol")
        elif self.tamano == 1 and self.raiz.clave == clave:
            self.raiz = None
            self.tamano = self.tamano - 1
        else:
            raise KeyError("Error, la clave no está en el árbol")

    def remover(self, nodoActual):
        # Verifica si el nodo actual es una hoja (no tiene hijos)
        if nodoActual.esHoja():
            # Caso 1: El nodo a eliminar es una hoja
            if nodoActual == nodoActual.padre.hijoIzquierdo:
                nodoActual.padre.hijoIzquierdo = None
            else:
                nodoActual.padre.hijoDerecho = None

        # Verifica si el nodo actual tiene dos hijos
        elif nodoActual.tieneAmbosHijos():
            # Caso 2: El nodo a eliminar tiene dos hijos
            # En este caso, se encuentra el sucesor inmediato del nodo a eliminar,
            # se "empalma" el sucesor en lugar del nodo a eliminar, y se copian los datos del sucesor.
            suc = nodoActual.encontrarSucesor()
            suc.empalmar()
            nodoActual.clave = suc.clave
            nodoActual.cargaUtil = suc.cargaUtil

        else:
            # Caso 3: El nodo a eliminar tiene un solo hijo
            if nodoActual.tieneHijoIzquierdo():
                # Caso 3.1: El nodo a eliminar tiene un hijo izquierdo
                if nodoActual.esHijoIzquierdo():
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
                elif nodoActual.esHijoDerecho():
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
                else:
                    # Caso especial: nodoActual no es hijo de su padre
                    nodoActual.reemplazarDatoDeNodo(
                        nodoActual.hijoIzquierdo.clave,
                        nodoActual.hijoIzquierdo.cargaUtil,
                        nodoActual.hijoIzquierdo.hijoIzquierdo,
                        nodoActual.hijoIzquierdo.hijoDerecho,
                    )
            else:
                # Caso 3.2: El nodo a eliminar tiene un hijo derecho
                if nodoActual.esHijoIzquierdo():
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
                elif nodoActual.esHijoDerecho():
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
                else:
                    # Caso especial: nodoActual no es hijo de su padre
                    nodoActual.reemplazarDatoDeNodo(
                        nodoActual.hijoDerecho.clave,
                        nodoActual.hijoDerecho.cargaUtil,
                        nodoActual.hijoDerecho.hijoIzquierdo,
                        nodoActual.hijoDerecho.hijoDerecho,
                    )


    def __delitem__(self, clave):
        self.eliminar(clave)


# --------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------
