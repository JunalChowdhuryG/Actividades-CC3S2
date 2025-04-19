# clase Producto 
class Producto:
    def __init__(self, nombre, precio, stock=10):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __repr__(self):
        return f"Producto({self.nombre}, {self.precio}, {self.stock})"