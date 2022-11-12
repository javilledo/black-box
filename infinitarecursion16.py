import json

fichero = "test.fiabledb"

datos = [
    {
        "id": 1,
        "rev": 1,
        "value": {"nombre": "Blanca", "edad": 34},
    },
    {
        "id": 2,
        "rev": 1,
        "value": {"nombre": "Juan", "edad": 22},
    }
]

nuevo_dato_01 = {"nombre": "María","edad": 34}
nuevo_dato_02 = {"nombre": "Juan","edad": 22}
nuevo_dato_03 = {"nombre": "Marcos","edad": 49}
nuevo_dato_04 = {"nombre": "Juan", "edad": 22}

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

def insertar_en_disco(nuevo_dato: dict, fichero: str) -> list[dict[int,int, dict]]:

    f = open(fichero)
    with open(fichero, encoding='utf-8') as f:
        data = json.load(f)

    # init values
    last_id = 0
    last_rev = 0

    # get last ID
    last_id = 0
    last_id = max(map(lambda el: el["id"], data))

    # get last rev if data exists
    list_bool_exists = list(map(lambda el: (el["value"] ==  nuevo_dato), data))
    indexes_bool_exists = list(map(lambda idx: idx[0] if idx[1] == True else None, enumerate(list_bool_exists)))
    indexes_bool_exists = list(filter(lambda el: el is not None, indexes_bool_exists))
    if len(indexes_bool_exists) > 0:
        last_rev = data[indexes_bool_exists[-1]]["rev"]
    
    data.append(
        {
            "id": last_id + 1,
            "rev": last_rev + 1,
            "value": nuevo_dato
        }
    )

    with open(fichero,'w',encoding = 'utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    f.close()

    return data

guardar_a_disco(datos, fichero)
insertar_en_disco(nuevo_dato_01, fichero)
insertar_en_disco(nuevo_dato_02, fichero)
insertar_en_disco(nuevo_dato_03, fichero)
insertar_en_disco(nuevo_dato_04, fichero)