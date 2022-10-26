from functools import reduce
from math import floor

monedas = (500, 200, 100, 50, 20, 10, 5, 2, 1)

def calcular_cambio(cantidad: int) -> dict:
    
    monedas_cambio = dict.fromkeys(monedas, 0)

    monedas_cambio = calcular_cambio_recursive(monedas_cambio, cantidad, 0)

    return monedas_cambio


def calcular_cambio_recursive(monedas_cambio: dict, cantidad_restante: int, index: int) -> dict:

    moneda_valor = list(monedas_cambio.keys())[index]

    moneda_cantidad = floor(cantidad_restante / moneda_valor)
    cantidad_restante = cantidad_restante - moneda_cantidad * moneda_valor

    monedas_cambio[moneda_valor] = moneda_cantidad

    if(cantidad_restante > 0): 
        index += 1
        if(index >= len(list(monedas_cambio.keys()))): return monedas_cambio
        monedas_cambio = calcular_cambio_recursive(monedas_cambio, cantidad_restante, index)

    return monedas_cambio

def obtener_cantidad_total(monedas_cambio: dict) -> int:

    monedas_valores = list(monedas_cambio.keys())
    
    return sum(list(map(lambda moneda_valor: monedas_cambio[moneda_valor] * moneda_valor, monedas_valores)))


# Tests
assert obtener_cantidad_total(calcular_cambio(143)) == 143