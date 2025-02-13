# Integració continua

from src.factorial import factorial
import pytest

def test_factorial_1():
    assert factorial(1) == 1

def test_no_entero():

    # Si passem una cadena
    with pytest.raises(TypeError):
        factorial("a")

    # Si passem un float
    with pytest.raises(TypeError):
        factorial(3.5)

    # Si passem un booleà
    with pytest.raises(TypeError):
        factorial(True)

def test_negativo():
    with pytest.raises(ValueError):
        factorial(-5)

def test_5():
    assert factorial(5) == 120