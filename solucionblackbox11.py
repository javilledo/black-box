
recursos_humanos = [
    {"nombre": "Juan", "edad": 18},
    {"nombre": "Ana", "edad": 20},
    {"nombre": "Pedro", "edad": 27},
    {"nombre": "Luis", "edad": 28},
    {"nombre": "Maria", "edad": 33},
    {"nombre": "Jose", "edad": 34},
    {"nombre": "Rosa", "edad": 41},
    {"nombre": "Luisa", "edad": 44},
    {"nombre": "Ramon", "edad": 45},
    {"nombre": "Marta", "edad": 52},
    {"nombre": "Pablo", "edad": 61},
]

def encontrar_por_busqueda_binaria(lista: tuple[dict[str, int]], edad_a_buscar: int) -> str:
    return recursive_compare(lista, edad_a_buscar, [0, len(lista)])


def recursive_compare(lista: tuple[dict[str, int]], edad_a_buscar: int, index_range: list[int, int]) -> str:

    index = index_range[0] + int((index_range[-1] - index_range[0]) / 2)

    value = lista[index]["edad"]

    if(value == edad_a_buscar):  return lista[index]["nombre"]
    elif(value < edad_a_buscar): return recursive_compare(lista, edad_a_buscar, [index + 1, index_range[-1]])
    elif(value > edad_a_buscar): return recursive_compare(lista, edad_a_buscar, [index_range[0], index - 1])   
    else: return 'No se ha encontrado ninguna coincidencia'  

# TEST
assert encontrar_por_busqueda_binaria(recursos_humanos, 20) == 'Ana'
assert encontrar_por_busqueda_binaria(recursos_humanos, 27) == 'Pedro'
assert encontrar_por_busqueda_binaria(recursos_humanos, 61) == 'Pablo'