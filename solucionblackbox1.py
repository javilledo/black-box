
def filtro_por_anyo(secuencia: list[str], anyo: int) -> list[str]:
    return [el for el in secuencia if el[0:4] == str(anyo)]

res = filtro_por_anyo(["2020-1-4", "2019-4-7", "2021-12-11", "2020-8-9"], 2020)
# ["2020-1-4", "2020-8-9"]

print(res)