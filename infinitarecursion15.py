
import json
from infinitarecursionDatamodel import InfinitaRecursionData as IRD

fichero = "test.fiabledb"

datos = [
    {
        "id": 1,
        "value": {"nombre": "Blanca", "edad": 34},
        "version": 0
    },
    {
        "id": 2,
        "value": {"nombre": "Juan", "edad": 22},
        "version": 0
    }
]

def guardar_a_disco(datos: list[dict[int, dict, int]], fichero: str) -> bool:
    f = open(fichero)
    with open(fichero,'w',encoding = 'utf-8') as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)
    f.close()
    return True

def recuperar_de_disco(fichero: str) -> list[dict[int, dict, int]]:
    f = open(fichero)
    with open(fichero, encoding='utf-8') as f:
        data = json.load(f)
    f.close()
    return data

def recuperar_de_disco_asIRD(fichero: str) -> list[IRD]:
    f = open(fichero)
    with open(fichero, encoding='utf-8') as f:
        data = json.load(f)
    f.close()
    data_asIRD= list(map(lambda el: IRD.from_dict(el), data))
    return data_asIRD

guardar_a_disco(datos, fichero)
print(recuperar_de_disco(fichero))
print(recuperar_de_disco_asIRD(fichero))





