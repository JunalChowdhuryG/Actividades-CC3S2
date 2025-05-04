# test_stack.py

import pytest
from src.stack import Stack

def test_is_empty():
    stack = Stack()
    assert stack.is_empty() == True  # La pila recién creada debe estar vacía
    stack.push(5)
    assert stack.is_empty() == False  # Después de agregar un elemento, la pila no debe estar vacía

def test_push():
    stack = Stack()
    stack.push(1)
    assert stack.peek() == 1  # El valor recién agregado debe estar en la parte superior
    stack.push(2)
    assert stack.peek() == 2  # Después de otro push, el valor superior debe ser el último agregado

def test_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2  # El valor superior (2) debe eliminarse y devolverse
    assert stack.peek() == 1  # Después de pop(), el valor superior debe ser 1
    stack.pop()
    assert stack.is_empty() == True  # Después de eliminar todos los elementos, la pila debe estar vacía

def test_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2  # El valor superior debe ser el último agregado (2)
    assert stack.peek() == 2  # La pila no debe cambiar después de peek()

# Prueba adicional para manejar casos de error
def test_pop_empty():
    stack = Stack()
    with pytest.raises(IndexError, match="La pila está vacía"):
        stack.pop()

def test_peek_empty():
    stack = Stack()
    with pytest.raises(IndexError, match="La pila está vacía"):
        stack.peek()