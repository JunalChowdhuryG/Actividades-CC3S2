import pytest
from src.carrito import Carrito
from src.factories import ProductoFactory
from src.carrito import Carrito
from src.itemCarrito import ItemCarrito
from src.producto import Producto

"""
se tomo como ejemplo el repositorio
https://github.com/coady/pytest-parametrized
"""


# parametros test aplica descuento
@pytest.mark.parametrize(
    "precio, cantidad, porcentaje, total_esperado",
    [
        (100.0, 1, 0, 100.0),     #sin descuento
        (100.0, 2, 10, 180.0),    #200-20=180
        (50.0, 4, 25, 150.0),     #200-50=150
        (120.0, 1, 100, 0.0),     #descuento total
    ]
)
# test para aplicar descuento parametrizado
def test_aplicar_descuento_parametrizado(precio, cantidad, porcentaje, total_esperado, carrito):
    """
    AAA:
    Arrange:  crea un producto y se agrega al carrito
    Act:  aplica el descuento parametrizado
    Assert:  compara contra el total esperado
    """
    producto = ProductoFactory(precio=precio, stock=10)
    carrito.agregar_producto(producto, cantidad=cantidad)

    total_descuento = carrito.aplicar_descuento(porcentaje)
    assert total_descuento == total_esperado


# parametros test actualizar cantidad
@pytest.mark.parametrize(
    "cantidad_inicial, nueva_cantidad, esperado, debe_fallar",
    [
        (2, 5, 5, False),   # actualizacion valida
        (3, 0, 0, False),   # eliminacion cantidad a 0
        (1, -1, None, True) # error cantidad negativa
    ]
)
# test para actualizar catidad parametrizado
def test_actualizar_cantidad_parametrizado(carrito, cantidad_inicial, nueva_cantidad, esperado, debe_fallar):
    """
    AAA:
    Arrange: crea un producto y se agrega al carrito
    Act: actualiza la cantidad
    Assert: verifica resultado esperado o excepcion
    """
    producto = ProductoFactory(stock=10)
    carrito.agregar_producto(producto, cantidad=cantidad_inicial)

    if debe_fallar:
        with pytest.raises(ValueError):
            carrito.actualizar_cantidad(producto, nueva_cantidad)
    else:
        carrito.actualizar_cantidad(producto, nueva_cantidad)
        item = carrito.obtener_items()[0] if nueva_cantidad > 0 else None
        if item:
            assert item.cantidad == esperado
        else:
            assert carrito.obtener_items() == []


# parametrostest aplicar descuento condicional
@pytest.mark.parametrize(
    "precio, cantidad, porcentaje, minimo, total_esperado",
    [
        (200.0, 3, 10, 500, 540.0),  # aplica desc  600 >= 500 
        (150.0, 2, 15, 400, 300.0),  #no aplica desc 300 < 400 
    ]
)
# test para aplicar descuento condicional paraametrizado
def test_aplicar_descuento_condicional_parametrizado(precio, cantidad, porcentaje, minimo, total_esperado, carrito):
    producto = ProductoFactory(precio=precio, stock=10)
    carrito.agregar_producto(producto, cantidad)
    total = carrito.aplicar_descuento_condicional(porcentaje, minimo)
    assert total == total_esperado
