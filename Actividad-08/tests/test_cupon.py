# tests/test_cupon.py
import pytest
from src.carrito import Carrito
from src.factories import ProductoFactory

def test_aplicar_cupon_con_limite():
    """
    Red: Se espera que al aplicar un cupón, el descuento no supere el límite máximo.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Producto", precio=200.00)
    carrito.agregar_producto(producto, cantidad=2)  # Total = 400

    # Act
    total_con_cupon = carrito.aplicar_cupon(20, 50)  # 20% de 400 = 80, pero límite es 50

    # Assert
    assert total_con_cupon == 350.00


# parametros test aplicar_cupon_parametrizado
@pytest.mark.parametrize(
    "precio, cantidad, porcentaje, maximo, esperado",
    [
        (100.0, 5, 10, 100, 450.0),  # 500 - 50
        (100.0, 5, 50, 30, 470.0),   # 500 - 30 (limita el descuento)
        (200.0, 1, 100, 200, 0.0),   # 200 - 200
        (50.0, 4, 25, 20, 180.0),    # 200 - 20 (25% da 50, pero límite = 20)
    ]
)
# test aplicar_cupon_parametrizado
def test_aplicar_cupon_parametrizado(carrito, precio, cantidad, porcentaje, maximo, esperado):
    producto = ProductoFactory(precio=precio)
    carrito.agregar_producto(producto, cantidad)
    total = carrito.aplicar_cupon(porcentaje, maximo)
    assert total == esperado