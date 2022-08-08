
def ocultar_numeros(numeros: str|int, char_hide: str = "x") -> str:
    numeros = str(numeros).replace(" ", "")
    if len(numeros) != 16: return False
    return 'xxxxxxxxxxxxx' + numeros[-3:]

#Tests
assert ocultar_numeros(1234567890123456) == 'xxxxxxxxxxxxx456'
assert ocultar_numeros("1234567890123456") == 'xxxxxxxxxxxxx456'
assert ocultar_numeros("1234 5678 9012 3456") == 'xxxxxxxxxxxxx456'
assert ocultar_numeros(12345678901234567) == False
assert ocultar_numeros("12345678901234567") == False
assert ocultar_numeros("1234 5678 9012 3456 7") == False