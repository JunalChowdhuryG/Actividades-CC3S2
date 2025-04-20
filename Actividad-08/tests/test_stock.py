# tests/test_stock.py
import pytest
from src.carrito import Carrito
from src.producto import Producto

def test_agregar_producto_excede_stock():
    """
    Red: Se espera que al intentar agregar una cantidad mayor a la disponible en stock se lance un ValueError.
    """
    # Arrange
    producto = Producto("ProductoStock", 100.00, stock=5)
    carrito = Carrito()

    # Act & Assert
    with pytest.raises(ValueError):
        carrito.agregar_producto(producto, cantidad=6)


def test_agregar_producto_dentro_del_stock(carrito, producto_generico):
    """
    AAA:
    Arrange:  crea un producto con stock suficiente
    Act:  agrega dentro del limite
    Assert:  verifica que se agrego correctamente
    """
    # Arrange
    # Act
    carrito.agregar_producto(producto_generico, cantidad=3)

    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 3


def test_agregar_producto_excede_stock_lanza_error(carrito, producto_generico):
    """
    AAA:
    Arrange:  crea un producto con stock limitado
    Act y Assert:  intenta agregar mas del stock y se lanza un ValueError
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=1)

    # Act & Assert
    with pytest.raises(ValueError):
        carrito.agregar_producto(producto_generico, cantidad=11)  # Excede el stock
