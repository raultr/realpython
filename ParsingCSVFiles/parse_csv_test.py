import unittest
from parse_csv import leer_archivo_csv, obtener_minima_diferencia_de_goles, obtener_nombre


class AnalizaCSVTest(unittest.TestCase):

    def setUp(self):
        self.archivo_csv = './csv/football.csv'

    def test_leer_cabeceras_del_archivo_csv(self):
        self.assertEqual(
            leer_archivo_csv(self.archivo_csv)[0],
            ['Team', 'Games', 'Wins', 'Losses', 'Draws', 'Goals', 'Goals Allowed', 'Points']
            )

    def test_nombre_del_primer_equipo(self):
        self.assertEqual(leer_archivo_csv(self.archivo_csv)[1][0], 'Arsenal')

    def test_leer_puntos_del_primer_equipo(self):
        self.assertEqual(leer_archivo_csv(self.archivo_csv)[1][7], '87')

    def test_obtener_minima_diferencia_de_goles(self):
        parsed_data = [
            ['Team', 'Games', 'Wins', 'Losses', 'Draws', 'Goals', 'Goals Allowed', 'Points'],
            ['Arsenal', '38', '26', '9', '3', '79', '36', '87'],
            ['Liverpool', '38', '24', '8', '6', '67', '30', '80']
        ]

        self.assertEqual(obtener_minima_diferencia_de_goles(parsed_data), 1)

    def test_obtener_nombre_del_equipo(self):
        parsed_data = [
            ['Team', 'Games', 'Wins', 'Losses', 'Draws', 'Goals', 'Goals Allowed', 'Points'],
            ['Arsenal', '38', '26', '9', '3', '79', '36', '87'],
            ['Liverpool', '38', '24', '8', '6', '67', '30', '80']
        ]

        indice = obtener_minima_diferencia_de_goles(parsed_data)
        self.assertEqual(obtener_nombre(indice, parsed_data), 'Liverpool')

if __name__ == '__main__':
    unittest.main()
