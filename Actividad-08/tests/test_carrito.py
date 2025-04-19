# tests/test_carrito.py

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


if __name__ == "__main__":
    pytest.main()
