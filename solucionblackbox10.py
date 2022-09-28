
from functools import reduce
from emoji import is_emoji  

def caracteres_restantes_tuit(tuit: str) -> int:

    # La longitud máxima es de 280 caracteres.
    MAX_LENGTH = 280

    tuit_separated_by_words = tuit.split()
    count = sum(map(length_meassure, tuit_separated_by_words))

    # Los espacios cuentan como 1 carácter.
    count += len(tuit_separated_by_words) - 1

    # Código
    return MAX_LENGTH - count


def length_meassure(word: str) -> int:
    
    # Los emojis ocupan 2 caracteres.
    if is_emoji(word): return 2

    # Las URLs ocupan 23 caracteres (Twitter usa un acortador interno).
    if 'http' in word: return 23
    
    # Las letras cuentan como 1 carácter.
    return len(word)
    

assert caracteres_restantes_tuit("Hola") == 276
assert caracteres_restantes_tuit("Python 🐍") == 271
assert caracteres_restantes_tuit("Descarga Emacs en https://www.gnu.org/software/emacs/") == 239
