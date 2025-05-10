import unittest
from src.main import build_merkle_tree

class TestMerkleTree(unittest.TestCase):
    def test_merkle_tree_root(self):
        # Datos sencillos para probar la construcción del árbol.
        data = ["a", "b", "c", "d"]
        tree_root = build_merkle_tree(data)
        # Verificar que el hash de la raíz tiene 40 caracteres (típico de SHA-1).
        self.assertEqual(len(tree_root.hash_value), 40)

if __name__ == "__main__":
    unittest.main()
