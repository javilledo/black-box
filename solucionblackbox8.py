
def es_un_cuadrado_magico(matriz: tuple[tuple]) -> bool:
    
    matriz_list = list(map(lambda x: list(x), matriz))
    matriz_list_transpose = list(map(list, zip(*matriz_list)))

    sum_of_elements = list(map(lambda el: sum(el), matriz_list))
    sum_of_elements += list(map(lambda el: sum(el), matriz_list_transpose))
    sum_of_elements += [matriz_list[0][0] + matriz_list[1][1] + matriz_list[2][2], matriz_list[0][2] + matriz_list[1][1] + matriz_list[2][0]]

    are_all_the_same = len(set(sum_of_elements)) == 1

    return are_all_the_same

assert es_un_cuadrado_magico(((8, 1, 6), (3, 5, 7), (4, 9, 2))) == True
assert es_un_cuadrado_magico(((18, 23, 16), (17, 19, 21), (22, 15, 20))) == True
assert es_un_cuadrado_magico(((-2, 5, 3), (0, 9, 7), (6, 4, 1))) == False