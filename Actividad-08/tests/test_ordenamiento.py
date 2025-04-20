import pytest
from src.carrito import Carrito
from src.factories import ProductoFactory
from src.carrito import Carrito
from src.itemCarrito import ItemCarrito
from src.producto import Producto

def test_ordenar_items_por_nombre(carrito):
    """
    AAA:
    Arrange:  agregan productos en orden aleatorio por nombre
    Act:  ordenan por nombre
    Assert:  verifica que el orden es alfabetico
    """
    # Arrange
    producto_z = ProductoFactory(nombre="Zanahoria", precio=3.0, stock=10)
    producto_a = ProductoFactory(nombre="Arroz", precio=2.0, stock=10)
    producto_b = ProductoFactory(nombre="Banana", precio=1.0, stock=10)
    carrito.agregar_producto(producto_z)
    carrito.agregar_producto(producto_a)
    carrito.agregar_producto(producto_b)

    # Act
    items_ordenados = carrito.obtener_items_ordenados("nombre")

    # Assert
    nombres = [item.producto.nombre for item in items_ordenados]
    assert nombres == ["Arroz", "Banana", "Zanahoria"]


def test_ordenar_items_por_precio(carrito):
    """
    AAA:
    Arrange:  agregan productos con precios distintos
    Act:  ordenan por precio
    Assert: verifica que el orden es de menor a mayor precio
    """
    # Arrange
    producto_caro = ProductoFactory(nombre="PC Gamer", precio=1500.0, stock=10)
    producto_medio = ProductoFactory(nombre="Monitor", precio=300.0, stock=10)
    producto_barato = ProductoFactory(nombre="Mouse", precio=50.0, stock=10)

    carrito.agregar_producto(producto_caro)
    carrito.agregar_producto(producto_medio)
    carrito.agregar_producto(producto_barato)

    # Act
    items_ordenados = carrito.obtener_items_ordenados("precio")

    # Assert
    precios = [item.producto.precio for item in items_ordenados]
    assert precios == [50.0, 300.0, 1500.0]
