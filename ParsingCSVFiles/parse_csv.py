import csv


class ParseCSV(object):
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv

    def leer_archivo_csv(self):
        with open(self.archivo_csv, 'r') as f:
            parsed_data = [row for row in csv.reader(f.read().splitlines())]
        return parsed_data

    def obtener_minima_diferencia(self, parsed_data, columna1, columna2):
        goles = self.obtener_datos_columna(parsed_data, columna1)  # Lista de todos los goles
        goles_encontra = self.obtener_datos_columna(parsed_data, columna2)   # Lista de todos los goles encontra
        agrupar_datos = zip(goles, goles_encontra)  # Agrupamos los datos por su indice
        dfierencias_goles = [float(x) - float(y) for x, y in agrupar_datos]  # Calculamos la diferencia de goles y se regresa
        return dfierencias_goles.index(min(dfierencias_goles))

    def obtener_nombre(self, index_value, parsed_data):
        print(parsed_data[0])
        equipos = self.obtener_datos_columna(parsed_data, 0)
        return equipos[index_value]

    def obtener_datos_columna(self, parsed_data, columna):
        return [x[columna] for x in parsed_data[1:]]
