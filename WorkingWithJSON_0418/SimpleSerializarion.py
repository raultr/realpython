import json

def GuardarEstructuraEnArchivoJson():
    data = {
        "president": {
            "name": "Zaphod Beeblebrox",
            "species": "Betelgeusian"
        }
    }
    with open("data_file.json", "w") as write_file:
        #Se le pasa el objeto a serializar y el archivo donde se guardara
        json.dump(data, write_file)


GuardarEstructuraEnArchivoJson()
