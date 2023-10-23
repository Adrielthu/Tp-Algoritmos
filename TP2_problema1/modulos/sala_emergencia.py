from .monticulo import MonticuloBinario

class SalaEmergencia:
    def __init__(self):
        self.monticulo = MonticuloBinario()

    def ingresar_paciente(self, paciente):
        self.monticulo.insertar(paciente)

    def atender_paciente(self):
        paciente_atendido = self.monticulo.eliminarMin()
        return paciente_atendido

    def total_pacientes(self):
        return self.monticulo.tamanoActual

    def __iter__(self):
        return iter(self.monticulo)