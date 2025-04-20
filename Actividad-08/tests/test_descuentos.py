import pytest
from src.carrito import Carrito
from src.factories import ProductoFactory
from src.carrito import Carrito
from src.itemCarrito import ItemCarrito
from src.producto import Producto

def test_aplicar_descuento(carrito, producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con una cantidad determinada.
    Act: Se aplica un descuento del 10% al total.
    Assert: Se verifica que el total con descuento sea el correcto.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=2)  # Total 1000
    
    # Act
    total_con_descuento = carrito.aplicar_descuento(10)
    
    # Assert
    assert total_con_descuento == 180.0


def test_aplicar_descuento_limites(carrito, producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act y Assert: Se verifica que aplicar un descuento fuera del rango [0, 100] genere un error.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=1)
    
    # Act y Assert
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(150)
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(-5)


def test_descuento_condicional_aplicado(carrito, producto_generico):
    """
    AAA:
    Arrange:  agrega un producto con total mayor al minimo.
    Act:  aplica el descuento condicional.
    Assert:  verifica que el descuento se aplica correctamente.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=1)  # Total = 100
    
    # Act
    total_descuento = carrito.aplicar_descuento_condicional(15, minimo=50)
    
    # Assert
    assert total_descuento == 85.00


def test_descuento_condicional_no_aplicado(carrito, producto_generico):
    """
    AAA:
    Arrange: agrega un producto con total menor al minimo.
    Act: aplica el descuento condicional.
    Assert: verifica que el total no cambia.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=1)  # Total = 100

    # Act
    total_descuento = carrito.aplicar_descuento_condicional(30, minimo=200)

    # Assert
    assert total_descuento == 100.00