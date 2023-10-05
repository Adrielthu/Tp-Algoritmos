from .AVL import AVL
class TemperaturasDB:
    def __init__(self):
        self.avl = AVL()
    
    def guardar_temperatura(self,temperatura, fecha):
        self.avl.agregar(temperatura, fecha)

    def devolver_temperatura(self, fecha):
        pass
    
    def min_temp_rango(self, fecha1, fecha2):
        pass

    def temp_extremos_rango(self, fecha1, fecha2):
        pass

    def borrar_temperatura(self, fecha):
        pass

    def devolver_temperaturas(self, fecha1, fecha2):
        pass

    def cantidad_muestras(self):
        return self.avl.tamano