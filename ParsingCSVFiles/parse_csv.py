import csv


def leer_archivo_csv(data):
    with open(data, 'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
    return data


def obtener_minima_diferencia_de_goles(parsed_data):
    parsed_data.pop(0)
    goles = [x[5] for x in parsed_data] # Lista de todos los goles
    goles_encontra = [x[6]for x in parsed_data] # Lista de todos los goles encontra
    agrupar_datos = zip(goles, goles_encontra) # Agrupamos los datos por su indice
    dfierencias_goles = [float(x) - float(y) for x, y in agrupar_datos] # Calculamos la diferencia de goles y se regresa
    return dfierencias_goles.index(min(dfierencias_goles))


def obtener_nombre(index_value, parsed_data):
    equipos = [x[0] for x in parsed_data]
    return equipos[index_value]
