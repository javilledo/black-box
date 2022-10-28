
base_de_datos = [
    {"id": 1, "idioma": "Ingles"},
    {"id": 2, "idioma": "Frances"},
    {"id": 3, "idioma": "Aleman"},
    {"id": 4, "idioma": "Italiano"},
    {"id": 5, "idioma": "Portugues"},
    {"id": 6, "idioma": "Ruso"},
]

def mover_elemento(lista: list[dict[int, str]], indice: int, destino: int) -> list[dict[int, str]]:

    # Reorder elements
    temp = lista[indice]
    del lista[indice]
    lista.insert(destino, temp)

    # Renumber ids
    lista = list(map(change_id, enumerate(lista)))

    return lista

def change_id(idex_and_item):
    index,  item = idex_and_item
    return {"id": index + 1, "idioma": item["idioma"]}

# TESTS

base_de_datos_changed_1_5 = [
    {"id": 1, "idioma": "Ingles"},
    {"id": 2, "idioma": "Aleman"},
    {"id": 3, "idioma": "Italiano"},
    {"id": 4, "idioma": "Portugues"},
    {"id": 5, "idioma": "Ruso"},
    {"id": 6, "idioma": "Frances"},
]

assert mover_elemento(base_de_datos, 1, 5) == base_de_datos_changed_1_5
