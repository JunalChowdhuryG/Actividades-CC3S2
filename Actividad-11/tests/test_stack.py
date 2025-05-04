import pytest
from src.stack import Stack


def test_is_empty():
    stack = Stack()
    assert stack.is_empty()  # La pila recien creada debe estar vacia
    stack.push(5)
    # Despues de agregar un elemento, la pila no debe estar vacia
    assert not stack.is_empty()


def test_push():
    stack = Stack()
    stack.push(1)
    assert stack.peek() == 1  # El valor recien agregado debe estar en la parte superior
    stack.push(2)
    # Despues de otro push, el valor superior debe ser el ultimo agregado
    assert stack.peek() == 2


def test_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2  # El valor superior (2) debe eliminarse y devolverse
    assert stack.peek() == 1  # Despues de pop(), el valor superior debe ser 1
    stack.pop()
    # Despues de eliminar todos los elementos, la pila debe estar vacia
    assert stack.is_empty()


def test_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2  # El valor superior debe ser el ultimo agregado (2)
    assert stack.peek() == 2  # La pila no debe cambiar despues de peek()


# Prueba adicional para manejar casos de error
def test_pop_empty():
    stack = Stack()
    with pytest.raises(IndexError, match="La pila esta vacia"):
        stack.pop()


def test_peek_empty():
    stack = Stack()
    with pytest.raises(IndexError, match="La pila esta vacia"):
        stack.peek()
