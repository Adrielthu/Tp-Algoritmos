from .AVL import AVL

class TemperaturasDB:
    def __init__(self):
        self.avl = AVL()

    def guardar_temperatura(self,temperatura, fecha):
        self.avl.agregar(temperatura, fecha)

    def devolver_temperatura(self, fecha):
        self.avl.obtener(fecha)

    def max_temp_rango(self, fecha1, fecha2):
        max = self.avl.obtener(fecha1)
        for fecha in self.avl:
            if fecha >= fecha1 and fecha <=fecha2:
                if self.avl.obtener(fecha) > max:
                    max = self.avl.obtener(fecha)
        return max

    def min_temp_rango(self, fecha1, fecha2):
        min = self.avl.obtener(fecha1)
        for fecha in self.avl:
            if fecha >= fecha1 and fecha <=fecha2:
                if self.avl.obtener(fecha) < min:
                    min = self.avl.obtener(fecha)
        return min

    def temp_extremos_rango(self, fecha1, fecha2):
        return self.min_temp_rango(fecha1, fecha2), self.max_temp_rango(fecha1,fecha2)

    def borrar_temperatura(self, fecha):
        self.avl.eliminar(fecha)

    def devolver_temperaturas(self, fecha1, fecha2):
        for fecha in self.avl:
            if fecha >= fecha1 and fecha <=fecha2:
                print(f'{fecha.clave}: temperatura {fecha.cargaUtil}°C')

    def cantidad_muestras(self):
        return self.avl.tamano