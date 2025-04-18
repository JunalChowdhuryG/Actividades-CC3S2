import pytest
from src.belly import Belly

# test para la clase Belly

# test no gruñe si no ha comido nada 
def test_no_gruñe_si_no_ha_comido_nada():
    belly = Belly()
    belly.esperar(2)
    assert not belly.esta_gruniendo()

# test gruñe si ha comido mucho y espera
def test_gruñe_si_come_muchos_y_espera():
    belly = Belly()
    belly.comer(15)
    belly.esperar(2)
    assert belly.esta_gruniendo()

# test no gruñe si no espera
def test_no_gruñe_si_no_espera_lo_suficiente():
    belly = Belly()
    belly.comer(20)
    belly.esperar(1)
    assert not belly.esta_gruniendo()

# tesst si come fracciones pepinos
def test_comer_fraccionarios():
    belly = Belly()
    belly.comer(2.5)
    assert belly.pepinos_comidos == 2.5

# test cantidad de pepinos es positivo
def test_no_permite_negativos():
    belly = Belly()
    with pytest.raises(ValueError):
        belly.comer(-3)

# test cantidad de pepinos es mucho
def test_no_permite_demasiados():
    belly = Belly()
    with pytest.raises(ValueError):
        belly.comer(1001)

# test para la predicicion de gruñido
def test_prediccion_gruñido_true():
    belly = Belly()
    assert belly.predecir_gruñido(20, 2) == True

# test para la prediccion de gruñido con menos pepinos
def test_prediccion_gruñido_false():
    belly = Belly()
    assert belly.predecir_gruñido(5, 1.5) == False

# test para la reduccion de pepinos
def test_pepinos_restantes_para_gruñir():
    belly = Belly()
    belly.comer(8)
    assert belly.pepinos_para_gruñir() == 3

# test para la reduccion de pepinos si ya comio mucho
def test_pepinos_restantes_si_ya_come_mucho():
    belly = Belly()
    belly.comer(15)
    assert belly.pepinos_para_gruñir() == 0
