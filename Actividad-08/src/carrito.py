from .itemCarrito import ItemCarrito
# clase Carrito que representa un carrito de compras
class Carrito:
    def __init__(self):
        self.items = []

    # Agrega un producto al carrito. Si el producto ya existe, aumenta la cantidad.
    def agregar_producto(self, producto, cantidad=1):
        for item in self.items:
            if item.producto.nombre == producto.nombre:
                item.cantidad += cantidad
                return
        self.items.append(ItemCarrito(producto, cantidad))

    # Remueve un producto del carrito. Si la cantidad llega a 0, elimina el item.
    def remover_producto(self, producto, cantidad=1):
        for item in self.items:
            if item.producto.nombre == producto.nombre:
                if item.cantidad > cantidad:
                    item.cantidad -= cantidad
                elif item.cantidad == cantidad:
                    self.items.remove(item)
                else:
                    raise ValueError("Cantidad a remover es mayor que la cantidad en el carrito")
                return
        raise ValueError("Producto no encontrado en el carrito")

    # Actualiza la cantidad de un producto en el carrito. Si la nueva cantidad es 0, elimina el item.
    def actualizar_cantidad(self, producto, nueva_cantidad):
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        for item in self.items:
            if item.producto.nombre == producto.nombre:
                if nueva_cantidad == 0:
                    self.items.remove(item)
                else:
                    item.cantidad = nueva_cantidad
                return
        raise ValueError("Producto no encontrado en el carrito")

    # calcula el total del carrito sin descuento
    def calcular_total(self):
        return sum(item.total() for item in self.items)

    # calcula el total del carrito con descuento
    def aplicar_descuento(self, porcentaje):
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje debe estar entre 0 y 100")
        total = self.calcular_total()
        descuento = total * (porcentaje / 100)
        return total - descuento

    # cuenta el número total de items en el carrito
    def contar_items(self):
        return sum(item.cantidad for item in self.items)

    # devuelve una lista de los productos en el carrito
    def obtener_items(self):
        return self.items
    
    # vacia el carrito
    def vaciar(self):
        self.items = []

    # aplica un descuento condicional basado en el total del carrito
    def aplicar_descuento_condicional(self, porcentaje, minimo):
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje debe estar entre 0 y 100")

        total = self.calcular_total()
        if total >= minimo:
            descuento = total * (porcentaje / 100)
            return total - descuento
        return total

    # agrega un producto al carrito verificando el stock
    def agregar_producto(self, producto, cantidad=1):
        # verificar unidades en el carrito
        cantidad_en_carrito = 0
        for item in self.items:
            if item.producto.nombre == producto.nombre:
                cantidad_en_carrito = item.cantidad
                break

        if cantidad_en_carrito + cantidad > producto.stock:
            raise ValueError("excede el stock disponible")

        # si ya existe incrementa cantidad
        for item in self.items:
            if item.producto.nombre == producto.nombre:
                item.cantidad += cantidad
                return

        # si no existe agrega nuevo item
        self.items.append(ItemCarrito(producto, cantidad))


    def obtener_items_ordenados(self, criterio: str):
        if criterio == "nombre":
            return sorted(self.items, key=lambda item: item.producto.nombre)
        elif criterio == "precio":
            return sorted(self.items, key=lambda item: item.producto.precio)
        else:
            raise ValueError("criterio no valido")