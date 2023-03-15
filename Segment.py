from Point import Point

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
        	


    def __gt__(self, p):
        if self.y < p.y:
            return False
        elif self.y > p.y:
            return True
        else:
            if self.x < p.x:
                return True
            else:
                return False

