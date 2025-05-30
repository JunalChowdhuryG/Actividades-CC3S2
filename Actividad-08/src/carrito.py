from .itemCarrito import ItemCarrito
# clase Carrito que representa un carrito de compras
class Carrito:
    def __init__(self):
        self.items = []

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

    # funcion que busca un item en el carrito
    def _buscar_item(self, producto):
        for item in self.items:
            if item.producto.nombre == producto.nombre:
                return item
        return None


    # agrega un producto al carrito verificando el stock
    def agregar_producto(self, producto, cantidad=1):
        # verificar unidades en el carrito
        item = self._buscar_item(producto)
        cantidad_actual = item.cantidad if item else 0

        if cantidad_actual + cantidad > producto.stock:
            raise ValueError("excede el stock disponible")

        if item:
            item.cantidad += cantidad
        else:
            self.items.append(ItemCarrito(producto, cantidad))
    

    def obtener_items_ordenados(self, criterio: str):
        if criterio == "nombre":
            return sorted(self.items, key=lambda item: item.producto.nombre)
        elif criterio == "precio":
            return sorted(self.items, key=lambda item: item.producto.precio)
        else:
            raise ValueError("criterio no valido")
    
    # metodo calcula el total de impuestos del carrito
    def calcular_impuestos(self, porcentaje):
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje debe estar entre 0 y 100")
        total = self.calcular_total()
        return total * (porcentaje / 100)
    
    # metodo aplica un cupon de descuento al carrito
    def aplicar_cupon(self, descuento_porcentaje, descuento_maximo):
        if descuento_porcentaje < 0 or descuento_maximo < 0:
            raise ValueError("Los valores de descuento deben ser positivos")
        total = self.calcular_total()
        descuento_calculado = total * (descuento_porcentaje / 100)
        descuento_final = min(descuento_calculado, descuento_maximo)
        return total - descuento_final