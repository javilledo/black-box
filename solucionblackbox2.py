from random import shuffle

def generar_cubo_rubik_aleatorio() -> list[int]:
    result = [*range(0, 6)] * 9
    shuffle(result)
    return result

res = generar_cubo_rubik_aleatorio()
# [3, 5, 0, 2, 1, 4, 5, 0, 1, 2, 4, 1, 2, 1, 3, 5, 5, 4, 1, 3, 5, 3, 2, 4, 3, 0, 0, 2, 2, 3, 5, 3, 0, 0, 1, 1, 2, 4, 4, 3, 5, 4, 3, 0, 5, 4, 1, 5, 1, 4, 0, 2, 2, 0]

print(res)