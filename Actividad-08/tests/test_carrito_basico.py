import pytest
from src.carrito import Carrito
from src.factories import ProductoFactory
from src.carrito import Carrito
from src.itemCarrito import ItemCarrito
from src.producto import Producto


def test_agregar_producto_nuevo(carrito, producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se genera un producto.
    Act: Se agrega el producto al carrito.
    Assert: Se verifica que el carrito contiene un item con el producto y cantidad 1.
    """
    # Act
    carrito.agregar_producto(producto_generico)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].producto.nombre == "ProductoGenerico"
    assert items[0].cantidad == 1


def test_agregar_producto_existente_incrementa_cantidad(carrito, producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se agrega el mismo producto nuevamente aumentando la cantidad.
    Assert: Se verifica que la cantidad del producto se incrementa en el item.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=1)
    
    # Act
    carrito.agregar_producto(producto_generico, cantidad=2)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 3


def test_remover_producto(carrito, producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con cantidad 3.
    Act: Se remueve una unidad del producto.
    Assert: Se verifica que la cantidad del producto se reduce a 2.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=3)
    
    # Act
    carrito.remover_producto(producto_generico, cantidad=1)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 2


def test_remover_producto_completo(carrito, producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se remueve la totalidad de la cantidad del producto.
    Assert: Se verifica que el producto es eliminado del carrito.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=2)
    
    # Act
    carrito.remover_producto(producto_generico, cantidad=2)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0


def test_actualizar_cantidad_producto(carrito, producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto a 5.
    Assert: Se verifica que la cantidad se actualiza correctamente.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=1)
    
    # Act
    carrito.actualizar_cantidad(producto_generico, nueva_cantidad=5)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 5


def test_actualizar_cantidad_a_cero_remueve_producto(carrito, producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto a 0.
    Assert: Se verifica que el producto se elimina del carrito.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=3)
    
    # Act
    carrito.actualizar_cantidad(producto_generico, nueva_cantidad=0)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0


def test_calcular_total(carrito, productos_dobles):
    """
    AAA:
    Arrange: Se crea un carrito y se agregan varios productos con distintas cantidades.
    Act: Se calcula el total del carrito.
    Assert: Se verifica que el total es la suma correcta de cada item (precio * cantidad).
    """
    # Arrange
    carrito.agregar_producto(productos_dobles[0], cantidad=2)  # Teclado 80 * 2 = 160
    carrito.agregar_producto(productos_dobles[1], cantidad=1)  # Monitor 300 * 1 = 300
    
    # Act
    total = carrito.calcular_total()
    
    # Assert
    assert total == 460.00
