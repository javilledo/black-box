
disco = ((4, "Unicornio", 2), (3, "Pegasus", 6), (1, "Dragón", 3), (5, "Griffin", 4), (2, "Minotaur", 1), (6, "Quimera", 5))

def desfragmentar_disco(disco: tuple[int]) -> tuple[int]:

    elements = dict(map(lambda t: (t[0], t[1]), disco))

    next_elements = dict(map(lambda t: (t[0], t[2]), disco))

    result = tuple()

    result = recursive_add_elements(result, elements, next_elements)

    return result

def recursive_add_elements(result: tuple[int], elements: dict, next_elements: dict, aux = []):

    if len(result) == 0:
        aux.append(1)
        result += (tuple((1, elements[1], next_elements[1])),)
    
    next_element = next_elements[aux[-1]]
    aux.append(next_element)
    result += (tuple((next_element, elements[next_element], next_elements[next_element])),)
    
    if(len(aux) < len(elements.keys())):
        result = recursive_add_elements(result, elements, next_elements, aux)
    
    return result

assert desfragmentar_disco(disco) == ((1, "Dragón", 3), (3, "Pegasus", 6), (6, "Quimera", 5), (5, "Griffin", 4), (4, "Unicornio", 2), (2, "Minotaur", 1))
