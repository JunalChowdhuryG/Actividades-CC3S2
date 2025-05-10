#!/usr/bin/env python3
import hashlib

class MerkleTreeNode:
    """
    Representa un nodo en un árbol de Merkle.
    Cada nodo almacena un hash y, si no es hoja, referencia a sus nodos hijos.
    """
    def __init__(self, left=None, right=None, hash_value=None):
        self.left = left
        self.right = right
        self.hash_value = hash_value

def compute_hash(data):
    """
    Calcula el hash SHA-1 de la cadena dada.
    Se usa SHA-1 para asemejar la identificación de objetos en Git.
    """
    return hashlib.sha1(data.encode('utf-8')).hexdigest()

def build_merkle_tree(leaves):
    """
    Construye el árbol de Merkle a partir de una lista de datos.
    Cada dato se transforma en una hoja cuyo hash se calcula, y luego se combinan
    pares de hojas para formar nodos padre hasta obtener la raíz.
    
    Si el número de nodos en un nivel es impar, se duplica el último nodo.
    """
    if not leaves:
        return None
    # Convertir cada hoja en un nodo con el hash calculado.
    nodes = [MerkleTreeNode(hash_value=compute_hash(leaf)) for leaf in leaves]
    
    # Combinar pares de nodos hasta obtener la raíz.
    while len(nodes) > 1:
        temp_nodes = []
        # Si el número de nodos es impar, duplicar el último nodo.
        if len(nodes) % 2 != 0:
            nodes.append(nodes[-1])
        for i in range(0, len(nodes), 2):
            combined_data = nodes[i].hash_value + nodes[i+1].hash_value
            parent_hash = compute_hash(combined_data)
            parent = MerkleTreeNode(left=nodes[i], right=nodes[i+1], hash_value=parent_hash)
            temp_nodes.append(parent)
        nodes = temp_nodes
    return nodes[0]

def print_tree(node, level=0):
    """
    Imprime la estructura del árbol de Merkle de forma recursiva.
    """
    if node is not None:
        print("  " * level + f"Hash: {node.hash_value}")
        print_tree(node.left, level + 1)
        print_tree(node.right, level + 1)

def main():
    # Datos de ejemplo simulando el contenido de archivos (blobs)
    data = [
        "Contenido de archivo 1",
        "Contenido de archivo 2",
        "Contenido de archivo 3",
        "Contenido de archivo 4"
    ]
    # Construir el árbol de Merkle
    tree_root = build_merkle_tree(data)
    # Mostrar el hash de la raíz y la estructura completa del árbol
    print("Merkle Tree Root Hash:", tree_root.hash_value)
    print("\nEstructura del Merkle Tree:")
    print_tree(tree_root)

if __name__ == "__main__":
    main()