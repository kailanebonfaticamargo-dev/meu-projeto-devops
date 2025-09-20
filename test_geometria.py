import math
from geometria import area_quadrado, area_circulo

def test_area_quadrado_positivo():
    assert area_quadrado(3) == 9

def test_area_quadrado_zero():
    assert area_quadrado(0) == 0

def test_area_quadrado_negativo():
    assert area_quadrado(-4) == 16  # lado negativo tratado como positivo?

def test_area_circulo_positivo():
    assert math.isclose(area_circulo(2), 12.566370614359172, rel_tol=1e-9)

def test_area_circulo_zero():
    assert area_circulo(0) == 0
