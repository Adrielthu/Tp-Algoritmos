from TP2_problema2.modulos.entorno import TemperaturasDB


registro = TemperaturasDB()

registro.guardar_temperatura(30,'07/10/2023')
registro.guardar_temperatura(23,'08/10/2023')
registro.guardar_temperatura(13,'09/10/2023')
registro.guardar_temperatura(40,'30/12/2023')

registro.devolver_temperaturas('07/10/2023','30/12/2023')

print(f'{registro.max_temp_rango("07/10/2023","30/12/2023")}°C')
print(f'{registro.min_temp_rango("07/10/2023","30/12/2023")}°C')

print(f'{registro.temp_extremos_rango("07/10/2023","30/12/2023")}')

registro.borrar_temperatura('09/10/2023')

print(f'Cantidad de muestras: {registro.cantidad_muestras()}')