from Point import Point
import matplotlib.pyplot as plt

class Segment():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __lt__(self, s):
        """Segmentos más a la izquierda son menores.
        Esta sobrecarga sólo aplica para cuando recién
        se inserta un segmento en el árbol, no para
        cuando se hace swap porque los puntos de cruce
        son problemáticos."""
        if self.p1.x < s.p1.x:
            return True
        elif self.p1.x > s.p1.x:
            return False
        elif self.p1.y == s.p1.y: # Caso mismo punto inicial
            return self.p2.x < s.p2.x
        elif self.p1.y > s.p1.y:
            return self.p2.x < s.p1.x
        else:
            return self.p1.x < s.p2.x
    
    def dibujar(self, label = None):
        plt.plot([self.p1.x, self.p2.x], [self.p1.y, self.p2.y], label = label)
        #return 1
        
        
    # Tal vez pueda usar el > para la comparacion
    # despues de un punto de cruce

