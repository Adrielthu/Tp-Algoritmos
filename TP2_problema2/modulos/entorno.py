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
        # Convierte las fechas a objetos de fecha (assumiendo que _fecha_obj realiza esta conversión)
        fecha1 = self._fecha_obj(fecha1)
        fecha2 = self._fecha_obj(fecha2)

        # Inicializa la temperatura máxima con la temperatura de fecha1
        max_temp = self.avl.obtener(fecha1)

        # Itera a través de las fechas en el AVL
        for fecha in self.avl:
            # Verifica si la fecha está dentro del rango especificado
            if fecha >= fecha1 and fecha <= fecha2:
                # Actualiza la temperatura máxima si se encuentra una temperatura mayor
                if self.avl.obtener(fecha) > max_temp:
                    max_temp = self.avl.obtener(fecha)

        # Retorna la temperatura máxima dentro del rango
        return max_temp

    # El método min_temp_rango sigue una lógica similar, pero busca la temperatura mínima en el rango.
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
        # Devuelve tanto la temperatura mínima como la máxima en el rango especificado
        return self.min_temp_rango(fecha1, fecha2), self.max_temp_rango(fecha1, fecha2)

    def borrar_temperatura(self, fecha):
        self.avl.eliminar(self._fecha_obj(fecha))

    def devolver_temperaturas(self, fecha1, fecha2):
        fecha1 = self._fecha_obj(fecha1)
        fecha2 = self._fecha_obj(fecha2)
    # Itera a través de las fechas en el AVL y muestra las temperaturas dentro del rango especificado
        for fecha in self.avl:
            if fecha >= fecha1 and fecha <=fecha2:
                print(f'{fecha}: temperatura {self.avl.obtener(fecha)}°C')

    def cantidad_muestras(self):
        return self.avl.tamano