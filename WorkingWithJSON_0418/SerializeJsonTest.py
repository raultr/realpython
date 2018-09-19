# python -m unittest -v SerializeJsonTest.py

import unittest
from SerializeJson import SerializacionSimple


class TestSerializacionSimple(unittest.TestCase):
    def setUp(self):
        self.Simple = SerializacionSimple()

        self.archivoDestino = "data_file.json"

        self.dicPythonOrigen = {
            "president": {
              "name": "Zaphod Beeblebrox",
              "species": "Betelgeusian"
            }
        }

        self.cadena_json = """{
    "president":{
        "name":"Zaphod Beeblebrox",
        "species":"Betelgeusian"
    }
}"""
        self.url = "https://jsonplaceholder.typicode.com/todos"

    def test_SerializacionDeserializacionSimple(self):
        self.Simple.ConvertirDiccionarioEnJson(self.dicPythonOrigen, self.archivoDestino)

        resultado_json = ''
        with open(self.archivoDestino, 'rt') as in_file:
            resultado_json = in_file.read()

        self.assertEqual(resultado_json, self.cadena_json)

        DicPythonDestino = self.Simple.ConvertirArchivoJsonEnDiccionario(self.archivoDestino)
        self.assertEqual(DicPythonDestino, self.dicPythonOrigen)

    def test_DeserializacionSimpleDeUnaCadenaDeTexto(self):
        DicPythonDestino = self.Simple.ConvertirCadenaJsonEnDiccionario(self.cadena_json)
        self.assertEqual(DicPythonDestino, self.dicPythonOrigen)

    def test_DeserializacionSimpleDesdeUnRequest(self):
        DicPythonDestino = self.Simple.ConvertirCadenaJsonEnDiccionarioDesdeUnRequest(self.url)
        self.assertEqual(len(DicPythonDestino), 200)

if __name__ == '__main__':
    unittest.main()
