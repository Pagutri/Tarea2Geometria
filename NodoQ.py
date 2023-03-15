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
        print(root.key[0].x, root.key[0].y, end=" ")
        inorder(root.right)
        
def nodo_minimo(nodo):
    """Devuelve el nodo con la minima coordenada Y,
    es decir, la hoja de mas a la izquierda."""
    current = nodo
    
    while current and current.left is not None:
        current = current.left

    return current
    

        
# Funcion buscar


# Funcion borrar


