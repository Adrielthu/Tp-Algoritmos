from TP2_problema3.modulos.entorno import EntornoRutas

ejemplo = EntornoRutas()

# Recibe como parámetro un archivo
ejemplo.construir_grafo("rutas.txt")

ejemplo.numeroDeVertices()

ejemplo.mostrar_caminos()

#Recibe como parámetro una ciudad de inicio y una de destino
ejemplo.precio_min("CiudadBs.As.", "VillaMercedes")


# ejemplo.graficar(usar_grafo_precio=True)

# ejemplo.graficar(usar_grafo_precio=False)
