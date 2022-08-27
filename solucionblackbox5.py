
from random import choice, choices, shuffle
import string

AZ_upper_case = list(string.ascii_uppercase)
AZ_lower_case = list(string.ascii_lowercase)
range_09 = list(str(range(10)))
special_chars = list('!@#$%^&*.')
all_chars = AZ_upper_case + AZ_lower_case + range_09 + special_chars

def generar_contrasenya(longitud: int) -> str:

    password = []

    password.append(choice(AZ_upper_case))
    password.append(choice(AZ_lower_case))
    password.append(choice(range_09))
    password.append(choice(special_chars))

    if longitud > 4:
        password += choices(all_chars, k = longitud - 4)

    shuffle(password)

    password = ''.join(password)

    return password

generar_contrasenya(10)
generar_contrasenya(6)
generar_contrasenya(2)
