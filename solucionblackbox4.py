
def formatear_precio(price: float|int) -> str:

    input = str(round(price, 2))

    decomp = input.split('.')

    if len(decomp) == 2:
        if decomp[1] == ('0' or '00'):
            decomp.pop()
        elif len(decomp[1]) == 1:
            decomp[1] = decomp[1] + '0'

    return ','.join(decomp)

#Tests
assert formatear_precio(8) == '8'
assert formatear_precio(1.0) == '1'
assert formatear_precio(1.5) == '1,50'
assert formatear_precio(2.03) == '2,03'
assert formatear_precio(0.4567) == '0,46'
assert formatear_precio(8.0) == '8'
assert formatear_precio(8.00) == '8'