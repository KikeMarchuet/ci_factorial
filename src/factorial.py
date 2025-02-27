
"""Mòdul funció factorial.
Integració Continua
"""

def factorial(num):

    """ Funció factorial
    que cumplís lo especificat aplicant recursivitat
    i contemplant els distints tests"""

    # Si no és un entero, té que donar error
    if not isinstance(num, int):
        raise TypeError("El número deu ser un entero")
    # Si és un booleà, té que donar error
    if isinstance(num, bool):
        raise TypeError("El número no pot ser un booleà")

    # Error si és negatiu
    if num < 0:
        raise ValueError("El número deu ser major que zero")

    # Situació base
    if num in (0, 1):
        return 1

    # Recursivitat
    return num * factorial(num - 1)  # Recursión
