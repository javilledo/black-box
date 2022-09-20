lista_numeros_repetidos = (5, 2, 6, 5, 5, 6, 3, 1, 4, 2, 4)

def eliminar_repetidos(lista: tuple) -> list:

    lista = list(lista)

    res = []

    res = list(map(lambda x: add_if_not_in_list(x, res= res), lista))[0]

    return res

def add_if_not_in_list(value: int, res: list) -> list:
    if value not in res: res.append(value)
    return res

assert eliminar_repetidos(lista_numeros_repetidos) == [5, 2, 6, 3, 1, 4]