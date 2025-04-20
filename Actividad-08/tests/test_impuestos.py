import pytest
from src.carrito import Carrito
from src.factories import ProductoFactory

def test_calcular_impuestos():
    """
    Red: Se espera que calcular_impuestos retorne el valor del impuesto.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Producto", precio=250.00)
    carrito.agregar_producto(producto, cantidad=4)  # Total=1000

    # Act
    impuesto = carrito.calcular_impuestos(10)  #10% de 1000=100

    # Assert
    assert impuesto == 100.00