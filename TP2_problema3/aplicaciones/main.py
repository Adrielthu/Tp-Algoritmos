from TP2_problema3.modulos.entorno import ServicioDeTransporte

ejemplo = ServicioDeTransporte()

# Recibe como parámetro un archivo
ejemplo.construir_grafo("rutas.txt")

ejemplo.numeroDeVertices()

ejemplo.mostrar_caminos()

#Recibe como parámetro una ciudad de inicio y una de destino
ejemplo.precio_min("Rafaela","CiudadBs.As.")

# Esta grafica es para tener una idea de las conexiones
# pero no representa el grafo real, ya que no puede hacer
# todas las aristas

#ejemplo.graficar()

