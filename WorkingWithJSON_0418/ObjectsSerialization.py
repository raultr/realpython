import json


class Elf:
    def __init__(self, level, ability_scores=None):
        self.level = level
        self.ability_scores = {
            "str": 11, "dex": 12, "con": 10,
            "int": 16, "wis": 14, "cha": 13
        } if ability_scores is None else ability_scores
        self.hp = 10 + self.ability_scores["con"]


class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, Elf):
            return (z.level, z.ability_scores, z.hp)
        else:
            super().default(self, z)


def encode_complex(z):
    if isinstance(z, Elf):
        return (z.level, z.ability_scores, z.hp)
    else:
        type_name = z.__class__.__name__
        raise TypeError(f"Object of type '{type_name}' is not JSON serializable")


def decode_complex(dct):
    if "__Elf__" in dct:
        return Elf(dct["level"])
    return dct

elf = Elf(level=4)
type(elf)
print(elf)
#json.dumps(elf)
#TypeError: Object of type 'Elf' is not JSON serializable
print("Usando una funcion")
a=json.dumps(elf, default=encode_complex)
print(a)
print("Usando la clase")
b=json.dumps(elf, cls=ComplexEncoder)
print(json.loads(b))
print("Leemos un objeto complejo desde un archivo")
with open("complex_data.json") as complex_data:
    data = complex_data.read()
    z = json.loads(data, object_hook=decode_complex)
type(z)
print(z)

