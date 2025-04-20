import pytest
from src.user_manager import UserManager

# test agregar usuario exitoso
def test_agregar_usuario_exitoso():
    # Arrange
    manager = UserManager()
    username = "junal"
    password = "securepassword"

    # Act
    manager.add_user(username, password)

    # Assert
    assert manager.user_exists(username), "El usuario debería existir después de ser agregado."