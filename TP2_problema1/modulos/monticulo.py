class MonticuloBinario:
    def __init__(self):
        # Inicializa un montículo binario como una lista con un elemento 0.
        self.listaMonticulo = [0]
        self.tamanoActual = 0

    def infiltArriba(self, i):
        # Realiza el proceso de filtrado hacia arriba (burbujeo) para mantener el orden del montículo.
        while i // 2 > 0:
            if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
            i = i // 2

    def insertar(self, k):
        # Inserta un elemento en el montículo y ajusta el orden mediante el filtrado hacia arriba.
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)

    def infiltAbajo(self, i):
        # Realiza el proceso de filtrado hacia abajo (heapify) para mantener el orden del montículo.
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            if self.listaMonticulo[i] > self.listaMonticulo[hm]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm

    def hijoMin(self, i):
        # Encuentra el índice del hijo con el valor mínimo.
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i * 2] < self.listaMonticulo[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def eliminarMin(self):
        # Elimina y retorna el valor mínimo del montículo, manteniendo su estructura.
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado

    def construirMonticulo(self, unaLista):
        # Construye un montículo a partir de una lista de elementos, manteniendo su propiedad de montículo.
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [0] + unaLista[:]
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1

    def __iter__(self):
        # Permite la iteración sobre los elementos del montículo, excluyendo el elemento 0 en la lista.
        for i in range(1, len(self.listaMonticulo)):
            yield self.listaMonticulo[i]
