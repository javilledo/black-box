from random import randint

mi_lista = ("Lisp", "Clojure", "Haskell", "Python", "Racket", "Elisp")

def desordenar_lista(lista: tuple[str]) -> tuple[str]:

    mi_lista_as_dict = list(map(lambda el: {'value': el, 'reordered': False}, mi_lista))

    lista_as_dict_reordered = move_random_element_to_end(mi_lista_as_dict)

    lista_reordered = list(map(lambda el: el['value'], lista_as_dict_reordered))
    
    return lista_reordered


def move_random_element_to_end(lista: tuple[str]) -> tuple[str]:

    list_of_reordered = list(map(lambda el: el['reordered'], lista))
    unique_elements = set(list_of_reordered)

    if (len(unique_elements) == 1):
        if(unique_elements == {True}): return lista

    random_index = randint(0, len(lista) - 1)
    lista[random_index]['reordered'] = True
    lista.append(lista[random_index]);
    del lista[random_index]

    return move_random_element_to_end(lista)

# Test
# Devuelve una lista pero en orden aleatorio
assert desordenar_lista(mi_lista) != mi_lista
# Devuelve una lista con los mismos elementos que mi_lista
for _ in range(100):
    assert set(desordenar_lista(mi_lista)) == set(mi_lista)