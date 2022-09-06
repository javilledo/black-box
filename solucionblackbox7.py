
dict_dec2hex = { 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

def rgb_a_hexadecimal(rojo: int, verde: int, azul: int) -> str:
    return '#' + int_to_hex(rojo) + int_to_hex(verde) + int_to_hex(azul)

def int_to_hex(n: int) -> str:
    b = n % 16
    a = int(n/16) % 16
    return dict_dec2hex[a] + dict_dec2hex[b]

assert rgb_a_hexadecimal(82, 31, 130) == '#521f82'
assert rgb_a_hexadecimal(255, 0, 0) == '#ff0000'
assert rgb_a_hexadecimal(255, 100, 22) == '#ff6416'