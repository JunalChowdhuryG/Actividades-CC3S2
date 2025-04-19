# tests/test_carrito.py

import pytest
from src.carrito import Carrito
from src.factories import ProductoFactory
from src.carrito import Carrito
from src.itemCarrito import ItemCarrito
from src.producto import Producto

def test_agregar_producto_nuevo():
    """
    AAA:
    Arrange: Se crea un carrito y se genera un producto.
    Act: Se agrega el producto al carrito.
    Assert: Se verifica que el carrito contiene un item con el producto y cantidad 1.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Laptop", precio=1000.00)
    
    # Act
    carrito.agregar_producto(producto)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].producto.nombre == "Laptop"
    assert items[0].cantidad == 1


def test_agregar_producto_existente_incrementa_cantidad():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se agrega el mismo producto nuevamente aumentando la cantidad.
    Assert: Se verifica que la cantidad del producto se incrementa en el item.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Mouse", precio=50.00)
    carrito.agregar_producto(producto, cantidad=1)
    
    # Act
    carrito.agregar_producto(producto, cantidad=2)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 3


def test_remover_producto():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con cantidad 3.
    Act: Se remueve una unidad del producto.
    Assert: Se verifica que la cantidad del producto se reduce a 2.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Teclado", precio=75.00)
    carrito.agregar_producto(producto, cantidad=3)
    
    # Act
    carrito.remover_producto(producto, cantidad=1)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 2


def test_remover_producto_completo():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se remueve la totalidad de la cantidad del producto.
    Assert: Se verifica que el producto es eliminado del carrito.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Monitor", precio=300.00)
    carrito.agregar_producto(producto, cantidad=2)
    
    # Act
    carrito.remover_producto(producto, cantidad=2)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0


def test_actualizar_cantidad_producto():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto a 5.
    Assert: Se verifica que la cantidad se actualiza correctamente.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Auriculares", precio=150.00)
    carrito.agregar_producto(producto, cantidad=1)
    
    # Act
    carrito.actualizar_cantidad(producto, nueva_cantidad=5)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 5


def test_actualizar_cantidad_a_cero_remueve_producto():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto a 0.
    Assert: Se verifica que el producto se elimina del carrito.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Cargador", precio=25.00)
    carrito.agregar_producto(producto, cantidad=3)
    
    # Act
    carrito.actualizar_cantidad(producto, nueva_cantidad=0)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0


def test_calcular_total():
    """
    AAA:
    Arrange: Se crea un carrito y se agregan varios productos con distintas cantidades.
    Act: Se calcula el total del carrito.
    Assert: Se verifica que el total es la suma correcta de cada item (precio * cantidad).
    """
    # Arrange
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Impresora", precio=200.00)
    producto2 = ProductoFactory(nombre="Escáner", precio=150.00)
    carrito.agregar_producto(producto1, cantidad=2)  # Total 400
    carrito.agregar_producto(producto2, cantidad=1)  # Total 150
    
    # Act
    total = carrito.calcular_total()
    
    # Assert
    assert total == 550.00


def test_aplicar_descuento():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con una cantidad determinada.
    Act: Se aplica un descuento del 10% al total.
    Assert: Se verifica que el total con descuento sea el correcto.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Tablet", precio=500.00)
    carrito.agregar_producto(producto, cantidad=2)  # Total 1000
    
    # Act
    total_con_descuento = carrito.aplicar_descuento(10)
    
    # Assert
    assert total_con_descuento == 900.00


def test_aplicar_descuento_limites():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act y Assert: Se verifica que aplicar un descuento fuera del rango [0, 100] genere un error.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Smartphone", precio=800.00)
    carrito.agregar_producto(producto, cantidad=1)
    
    # Act y Assert
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(150)
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(-5)

def test_vaciar_carrito():
    """
    AAA:
    Arrange: Se crea un carrito con varios productos.
    Act: Se vacia el carrito.
    Assert: Se verifica que no hay items y el total es 0.
    """
    # Arrange
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Producto1", precio=100.00)
    producto2 = ProductoFactory(nombre="Producto2", precio=200.00)
    carrito.agregar_producto(producto1, cantidad=2)
    carrito.agregar_producto(producto2, cantidad=1)
    
    # Act
    carrito.vaciar()
    
    # Assert
    assert carrito.obtener_items() == []
    assert carrito.calcular_total() == 0.0


def test_descuento_condicional_aplicado():
    """
    AAA:
    Arrange:  agrega un producto con total mayor al minimo.
    Act:  aplica el descuento condicional.
    Assert:  verifica que el descuento se aplica correctamente.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="TV", precio=600.00)
    carrito.agregar_producto(producto, cantidad=1)  # Total = 600
    
    # Act
    total_descuento = carrito.aplicar_descuento_condicional(15, minimo=500)
    
    # Assert
    assert total_descuento == 510.00


def test_descuento_condicional_no_aplicado():
    """
    AAA:
    Arrange: agrega un producto con total menor al minimo.
    Act: aplica el descuento condicional.
    Assert: verifica que el total no cambia.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="USB", precio=100.00)
    carrito.agregar_producto(producto, cantidad=1)  # Total = 100

    # Act
    total_descuento = carrito.aplicar_descuento_condicional(15, minimo=200)

    # Assert
    assert total_descuento == 100.00


def test_agregar_producto_dentro_del_stock():
    """
    AAA:
    Arrange:  crea un producto con stock suficiente
    Act:  agrega dentro del límite
    Assert:  verifica que se agregó correctamente
    """
    # Arrange
    producto = Producto("Notebook", 1200.00, stock=5)
    carrito = Carrito()

    # Act
    carrito.agregar_producto(producto, cantidad=3)

    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 3


def test_agregar_producto_excede_stock_lanza_error():
    """
    AAA:
    Arrange:  crea un producto con stock limitado
    Act y Assert:  intenta agregar mas del stock y se lanza un ValueError
    """
    # Arrange
    producto = Producto("Impresora", 600.00, stock=2)
    carrito = Carrito()
    carrito.agregar_producto(producto, cantidad=1)

    # Act & Assert
    with pytest.raises(ValueError):
        carrito.agregar_producto(producto, cantidad=2)  # Excede el stock


def test_ordenar_items_por_nombre():
    """
    AAA:
    Arrange:  agregan productos en orden aleatorio por nombre
    Act:  ordenan por nombre
    Assert:  verifica que el orden es alfabetico
    """
    # Arrange
    carrito = Carrito()
    prod_c = Producto("Zanahoria", 3.0, stock=10)
    prod_a = Producto("Arroz", 2.0, stock=10)
    prod_b = Producto("Banana", 1.0, stock=10)

    carrito.agregar_producto(prod_c)
    carrito.agregar_producto(prod_a)
    carrito.agregar_producto(prod_b)

    # Act
    items_ordenados = carrito.obtener_items_ordenados("nombre")

    # Assert
    nombres = [item.producto.nombre for item in items_ordenados]
    assert nombres == ["Arroz", "Banana", "Zanahoria"]


def test_ordenar_items_por_precio():
    """
    AAA:
    Arrange:  agregan productos con precios distintos
    Act:  ordenan por precio
    Assert: verifica que el orden es de menor a mayor precio
    """
    # Arrange
    carrito = Carrito()
    prod_caro = Producto("Gamer PC", 1500.0, stock=10)
    prod_medio = Producto("Monitor", 300.0, stock=10)
    prod_barato = Producto("Mouse", 50.0, stock=10)

    carrito.agregar_producto(prod_caro)
    carrito.agregar_producto(prod_medio)
    carrito.agregar_producto(prod_barato)

    # Act
    items_ordenados = carrito.obtener_items_ordenados("precio")

    # Assert
    precios = [item.producto.precio for item in items_ordenados]
    assert precios == [50.0, 300.0, 1500.0]


if __name__ == "__main__":
    pytest.main()
