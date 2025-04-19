import pytest
from src.carrito import Carrito
from src.factories import ProductoFactory

@pytest.fixture
def carrito():
    return Carrito()

@pytest.fixture
def producto_generico():
    return ProductoFactory(nombre="ProductoGenerico", precio=100.0, stock=10)

@pytest.fixture
def productos_dobles():
    return [
        ProductoFactory(nombre="Teclado", precio=80.0, stock=10),
        ProductoFactory(nombre="Monitor", precio=300.0, stock=10)
    ]