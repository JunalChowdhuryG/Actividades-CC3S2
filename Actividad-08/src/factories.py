import factory
from .producto import Producto
from .carrito import Carrito
from faker import Faker

# clase ProductoFactory que representa un producto de prueba
class ProductoFactory(factory.Factory):
    class Meta:
        model = Producto

    nombre = factory.Faker("word")
    precio = factory.Faker("pyfloat", left_digits=2, right_digits=2, positive=True)