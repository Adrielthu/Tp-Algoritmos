from .AVL import AVL
import datetime

class TemperaturasDB:
    def __init__(self):
        self.avl = AVL()

    def _fecha_obj(self, fecha):
        fecha_obj = datetime.datetime.strptime(fecha, "%d/%m/%Y")
        return fecha_obj

    def guardar_temperatura(self,temperatura, fecha):
        self.avl.agregar(self._fecha_obj(fecha), temperatura)

    def devolver_temperatura(self, fecha):
        self.avl.obtener(self._fecha_obj(fecha))

    def max_temp_rango(self, fecha1, fecha2):
        fecha1 = self._fecha_obj(fecha1)
        fecha2 = self._fecha_obj(fecha2)

        max = self.avl.obtener(fecha1)
        for fecha in self.avl:
            if fecha >= fecha1 and fecha <=fecha2:
                if self.avl.obtener(fecha) > max:
                    max = self.avl.obtener(fecha)
        return max

    def min_temp_rango(self, fecha1, fecha2):
        fecha1 = self._fecha_obj(fecha1)
        fecha2 = self._fecha_obj(fecha2)

        min = self.avl.obtener(fecha1)
        for fecha in self.avl:
            if fecha >= fecha1 and fecha <=fecha2:
                if self.avl.obtener(fecha) < min:
                    min = self.avl.obtener(fecha)
        return min

    def temp_extremos_rango(self, fecha1, fecha2):
        return self.min_temp_rango(fecha1, fecha2), self.max_temp_rango(fecha1,fecha2)

    def borrar_temperatura(self, fecha):
        self.avl.eliminar(self._fecha_obj(fecha))

    def devolver_temperaturas(self, fecha1, fecha2):
        fecha1 = self._fecha_obj(fecha1)
        fecha2 = self._fecha_obj(fecha2)

        for fecha in self.avl:
            if fecha >= fecha1 and fecha <=fecha2:
                print(f'{fecha}: temperatura {self.avl.obtener(fecha)}°C')

    def cantidad_muestras(self):
        return self.avl.tamano