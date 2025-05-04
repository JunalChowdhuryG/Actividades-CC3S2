# stack.py

from typing import Any

class Stack:
    def __init__(self):
        """Inicializa una pila vacía."""
        self.items = []

    def push(self, data: Any) -> None:
        """Añade un elemento a la parte superior de la pila."""
        self.items.append(data)

    def pop(self) -> Any:
        """Elimina y devuelve el elemento en la parte superior de la pila."""
        if self.is_empty():
            raise IndexError("La pila está vacía")
        return self.items.pop()

    def peek(self) -> Any:
        """Devuelve el elemento en la parte superior de la pila sin eliminarlo."""
        if self.is_empty():
            raise IndexError("La pila está vacía")
        return self.items[-1]

    def is_empty(self) -> bool:
        """Devuelve True si la pila está vacía, False si no lo está."""
        return len(self.items) == 0