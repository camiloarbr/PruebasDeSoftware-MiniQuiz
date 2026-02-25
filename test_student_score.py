import pytest
from student_score import evaluar_estudiante

#pruebas normales
def test_aprobado_normal():
    assert evaluar_estudiante(70, 1) == "APROBADO"

def test_reprobado_normal():
    assert evaluar_estudiante(40, 0) == "REPROBADO"

#pruebas de borde
def test_aprobado_borde():
    assert evaluar_estudiante(60, 0) == "APROBADO"

def test_sobresaliente_borde():
    assert evaluar_estudiante(90, 0) == "REPROBADO"

#pruebas de error
def test_nota_negativa():
    with pytest.raises(ValueError):
        evaluar_estudiante(-10, 0)

def test_faltas_negativas():
    with pytest.raises(ValueError):
        evaluar_estudiante(80, -1)

#regla de negocio
def test_descuento_faltas():
    assert evaluar_estudiante(65, 5) == "APROBADO"

def test_descuento_faltas_reprobado():
    assert evaluar_estudiante(62, 5) == "REPROBADO"