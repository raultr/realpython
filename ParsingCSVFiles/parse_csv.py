import csv


class ParseCSV(object):
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv

    def leer_archivo_csv(self):
        with open(self.archivo_csv, 'r') as f:
            parsed_data = [row for row in csv.reader(f.read().splitlines())]
        return parsed_data

    def obtener_minima_diferencia(self, parsed_data, columna1, columna2):
        parsed_data.pop(0)
        goles = [x[columna1] for x in parsed_data]  # Lista de todos los goles
        goles_encontra = [x[columna2]for x in parsed_data]  # Lista de todos los goles encontra
        agrupar_datos = zip(goles, goles_encontra)  # Agrupamos los datos por su indice
        dfierencias_goles = [float(x) - float(y) for x, y in agrupar_datos]  # Calculamos la diferencia de goles y se regresa
        return dfierencias_goles.index(min(dfierencias_goles))

    def obtener_nombre(self, index_value, parsed_data):
        print(parsed_data[0])
        equipos = [x[0] for x in parsed_data]
        return equipos[index_value]
