import json
import requests


class SerializacionSimple:
    dicTodos = {}

    def ConvertirDiccionarioEnJson(self, data, archivo_json):
        with open(archivo_json, "w") as write_file:
            # Se le pasa el objeto a serializar y el archivo donde se guardara
            # Tambien podemos especificarle si tendra identation
            json.dump(data, write_file, indent=4,  separators=(',', ':'))

    def ConvertirArchivoJsonEnDiccionario(self, archivo):
        print("***  Convertir archivo json en diccionario ****")
        with open("data_file.json", "r") as read_file:
            data = json.load(read_file)
        return data

    def ConvertirCadenaJsonEnDiccionario(self, json_str):
        return self.DeserializarJson(json_str)

    def ConvertirCadenaJsonEnDiccionarioDesdeUnRequest(self, url_json):
        response = requests.get(url_json)
        return self.DeserializarJson(response.text)

    def DeserializarJson(self, str_json):
        data = json.loads(str_json)
        return data
