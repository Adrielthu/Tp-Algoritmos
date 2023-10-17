class MonticuloBinarioTupla:
    def __init__(self):
        self.listaMonticulo = [(float('inf'),)]
        self.tamanoActual = 0

    def infiltArriba(self, i):
        while i // 2 > 0:
            if self.listaMonticulo[i][0] < self.listaMonticulo[i // 2][0]:
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
            i = i // 2

    def insertar(self, tupla):
        self.listaMonticulo.append(tupla)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)

    def infiltAbajo(self, i):
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            if self.listaMonticulo[i][0] > self.listaMonticulo[hm][0]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm

    def hijoMin(self, i):
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i * 2][0] < self.listaMonticulo[i * 2 + 1][0]:
                return i * 2
            else:
                return i * 2 + 1

    def eliminarMin(self):
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado

    def construirMonticulo(self, unaLista):
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [(float('inf'),)] + unaLista[:]
        i = len(unaLista) // 2
        while i > 0:
            self.infiltAbajo(i)
            i = i - 1

    def __iter__(self):
        for i in range(1, len(self.listaMonticulo)):
            yield self.listaMonticulo[i]

    def decrementarClave(self, tupla, nueva_clave):
        for i in range(1, len(self.listaMonticulo)):
            if self.listaMonticulo[i] == tupla:
                if nueva_clave > self.listaMonticulo[i][0]:
                    # No se puede aumentar la clave
                    return

                self.listaMonticulo[i] = (nueva_clave, *self.listaMonticulo[i][1:])
                self.infiltArriba(i)
                break
    
    def estaVacia(self):
        return self.tamanoActual == 0

