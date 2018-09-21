import unittest
from parse_csv import ParseCSV


class AnalizaCSVTest(unittest.TestCase):

    def setUp(self):
        self.footbal_csv = './csv/football.csv'
        self.weather_csv = './csv/weather.csv'
        self.football = ParseCSV(self.footbal_csv)
        self.weather = ParseCSV(self.weather_csv)

    def test_leer_cabeceras_del_archivo_csv(self):
        self.assertEqual(
            self.football.leer_archivo_csv()[0],
            ['Team', 'Games', 'Wins', 'Losses', 'Draws', 'Goals', 'Goals Allowed', 'Points']
            )

        self.assertEqual(
            self.weather.leer_archivo_csv()[0],
            ['Day', 'MxT', 'MnT', 'AvT', 'AvDP', '1HrP TPcpn', 'PDir', 'AvSp', 'Dir', 'MxS', 'SkyC', 'MxR', 'Mn', 'R AvSLP']
            )

    def test_leer_datos_aleatorios(self):
        self.assertEqual(self.football.leer_archivo_csv()[1][0], 'Arsenal')
        self.assertEqual(self.football.leer_archivo_csv()[1][7], '87')
        self.assertEqual(self.weather.leer_archivo_csv()[1][0], '1')
        self.assertEqual(self.weather.leer_archivo_csv()[1][7], '9.6')

    def test_nombre_del_primer_equipo(self):
        self.assertEqual(self.football.leer_archivo_csv()[1][0], 'Arsenal')

    def test_leer_puntos_del_primer_equipo(self):
        self.assertEqual(self.football.leer_archivo_csv()[1][7], '87')

    def test_obtener_minima_diferencia_de_goles(self):
        football_parsed_data = self.football.leer_archivo_csv()
        self.assertEqual(self.football.obtener_minima_diferencia(football_parsed_data, 5, 6), 19)

        weather_parsed_data = self.weather.leer_archivo_csv()
        self.assertEqual(self.football.obtener_minima_diferencia(weather_parsed_data, 1, 2), 13)

    def test_obtener_nombre_del_equipo(self):
        football_parsed_data = self.football.leer_archivo_csv()
        indice = self.football.obtener_minima_diferencia(football_parsed_data, 5, 6)
        self.assertEqual(self.football.obtener_nombre(indice, football_parsed_data), 'Leicester')

        weather_parsed_data = self.weather.leer_archivo_csv()
        indice = self.weather.obtener_minima_diferencia(weather_parsed_data, 1, 2)
        self.assertEqual(self.weather.obtener_nombre(indice, weather_parsed_data), '14')


if __name__ == '__main__':
    unittest.main()
