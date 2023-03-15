from Point import Point

class NodoQ:
    """Arbol binario para guardar los puntos evento. Cada nodo
    guarda el punto y el segmento que comienza en ese punto, o
    'None' si ningun segmento comienza en ese punto. El orden
    va de menor a mayor coordenada 'y' del punto. Puntos con la
    misma coordenada 'y' van de menor a mayor coordenada 'x'."""
    # Puede haber más de un segmento empezando ahi. Corregir.
    def __init__(self, punto, segmento):
        self.key = [punto, segmento]
        self.left = None
        self.right = None
        
def insertar(nodo, punto, segmento):
    # Crear nuevo nodo
    if nodo is None:
        return NodoQ(punto, segmento)

    if punto < nodo.key[0]:
        nodo.left = insertar(nodo.left, punto, segmento)
    else:
        nodo.right = insertar(nodo.right, punto, segmento)
        # El punto a insertar no puede tener las mismas coordenadas 
        # que la de ningun nodo en el arbol porque no queremos
        # repetir eventos. Escribir funcion 'buscar_en_arbol()'
        # y correrla antes de insertar() para evitar esto.
    return nodo

def inorder(root):
    if root is not None:
        inorder(root.left)
        print("(", root.key[0].x, root.key[0].y, end=") ")
        inorder(root.right)
        
def nodo_minimo(nodo):
    """Devuelve el nodo con la minima coordenada Y,
    es decir, la hoja de mas a la izquierda."""
    current = nodo
    
    while current and current.left is not None:
        current = current.left

    return current
    
def borrar_nodo(root, key):
    """key tiene que ser una lista con un punto y su(s) segmento(s)
    o su 'None'."""
    # base Case
    if root is None:
        return root

    # If the key to be deleted is
    # smaller than the root's key,
    # then it lies in left subtree
    if key[0] < root.key[0]:
        root.left = borrar_nodo(root.left, key)

    # If the key to be deleted is
    # greater than the root's key,
    # then it lies in right subtree
    elif key[0] > root.key[0]:
        root.right = borrar_nodo(root.right, key)

    # If key is same as root's key,
    # then this is the node
    # to be deleted
    else:

        # Node with only one child
        # or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children:
        # Get the inorder successor(smallest
        # in the right subtree)
        temp = nodo_minimo(root.right)

        # Copy the inorder successor's
        # content to this node
        root.key = temp.key

        # Delete the inorder successor
        root.right = borrar_nodo(root.right, temp.key)

    return root


def buscar_nodo(raiz, key):
    """Devuelve 'True' si el nodo se encuentra en el árbol
    y 'False' si no."""
    if raiz == None:
        return False
    if raiz.key[0] == key[0]:
        return True
    if key[0] < raiz.key[0]:
        return buscar_nodo(raiz.left, key)
    else:
        return buscar_nodo(raiz.right, key)


def nodo_maximo(raiz):
    current = raiz
    
    while current and current.right is not None:
        current = current.right

    return current
