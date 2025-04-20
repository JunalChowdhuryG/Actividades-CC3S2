
import pytest
from src.carrito import Carrito
from src.factories import ProductoFactory
from src.carrito import Carrito
from src.itemCarrito import ItemCarrito
from src.producto import Producto





def test_vaciar_carrito(carrito, productos_dobles):
    """
    AAA:
    Arrange: Se crea un carrito con varios productos.
    Act: Se vacia el carrito.
    Assert: Se verifica que no hay items y el total es 0.
    """
    # Arrange
    carrito.agregar_producto(productos_dobles[0], cantidad=2)
    carrito.agregar_producto(productos_dobles[1], cantidad=1)
    
    # Act
    carrito.vaciar()
    
    # Assert
    assert carrito.obtener_items() == []
    assert carrito.calcular_total() == 0.0
