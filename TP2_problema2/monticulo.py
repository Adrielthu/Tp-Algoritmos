class MonticuloBinario:
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0

    def infiltArriba(self,i):
        while i // 2 > 0:
           
            if self.listaMonticulo[i].get_riesgo < self.listaMonticulo[i // 2].get_riesgo:
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
            i = i // 2
    
    def insertar(self,k):
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)

    def infiltAbajo(self,i):
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            if self.listaMonticulo[i].get_riesgo > self.listaMonticulo[hm].get_riesgo:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm

    def hijoMin(self,i):
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i*2].get_riesgo < self.listaMonticulo[i*2+1].get_riesgo:
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
    
    def construirMonticulo(self,unaLista):
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [0] + unaLista[:]
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1
    
    def __iter__(self):
        for i in range(1,len(self.listaMonticulo)):
            yield self.listaMonticulo[i]

lista = [40,60,70,20,20]

monticulo = MonticuloBinario()
monticulo.construirMonticulo(lista)

#print(monticulo.eliminarMin())
print(monticulo.tamanoActual)

#monticulo.insertar(20)
print(monticulo.tamanoActual)

for x in monticulo:
    print (x)

