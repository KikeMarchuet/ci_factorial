
"""Mòdul funció factorial."""

def factorial(num):

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
    if num == 0 or num == 1:
        return 1

    # Recursivitat
    return num * factorial(num - 1)  # Recursión
