from TP2_problema3.modulos.entorno import ServicioDeTransporte

ejemplo = ServicioDeTransporte()

# Recibe como parámetro un archivo y crea el grafo
ejemplo.construir_rutas("rutas.txt")

# Retorna el numero de vertices
ejemplo.numeroDeCiudades()

#ejemplo.mostrar_caminos()

#Recibe como parámetro una ciudad de inicio y una de destino
ejemplo.precio_min("CiudadBs.As.", "LaRioja")

#ejemplo.graficar(usar_grafo_precio=True)

#ejemplo.graficar(usar_grafo_precio=False)
