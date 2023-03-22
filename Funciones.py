from Point import Point
from Segment import Segment

def on_segment(pi, pj, pk):
    if min(pi.x, pj.x) <= pk.x and pk.x <= max(pi.x, pj.x) \
       and min(pi.y, pj.y) <= pk.y and pk.y <= max(pi.y, pj.y):
        return True
    else:
        return False

def direction(pi, pj, pk):
    a = pk - pi
    b = pj - pi
    return a.x*b.y - a.y*b.x
    
def segments_intersect(s1, s2):
    d1 = direction(s2.p1, s2.p2, s1.p1)
    d2 = direction(s2.p1, s2.p2, s1.p2)
    d3 = direction(s1.p1, s1.p2, s2.p1)
    d4 = direction(s1.p1, s1.p2, s2.p2)
    
    if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and \
       ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
        return True
    elif d1 == 0 and on_segment(s2.p1, s2.p2, s1.p1):
        return True
    elif d2 == 0 and on_segment(s2.p1, s2.p2, s1.p2):
        return True
    elif d3 == 0 and on_segment(s1.p1, s1.p2, s2.p1):
        return True
    elif d4 == 0 and on_segment(s1.p1, s1.p2, s2.p2):
        return True
    else:
        return False


def punto_de_cruce(sa, sb):
    """Encuentra el punto de cruce una vez que se
    comprobó que los segmentos 'sa' y 'sb' sí se
    cruzan."""
    # Caso especial en que un segmento es vertical
    # y el otro es horizontal
    if sa.p1.x == sa.p2.x and sb.p1.y == sb.p2.y:
        x = sa.p1.x
        y = sb.p1.y 
    elif sb.p1.x == sb.p2.x and sa.p1.y == sa.p2.y:
        x = sb.p1.x
        y = sa.p1.y
    # En el resto de casos se evita dividir por cero
    elif sa.p1.x == sa.p2.x or sb.p1.x == sb.p2.x:
        ma = (sa.p2.x - sa.p1.x)/(sa.p2.y - sa.p1.y)
        mb = (sb.p2.x - sb.p1.x)/(sb.p2.y - sb.p1.y)
        y = (ma*sa.p1.y - mb*sb.p1.y + sb.p1.x - sa.p1.x)/(ma - mb)
        x = ma*(y - sa.p1.y) + sa.p1.x
    else:
        ma = (sa.p2.y - sa.p1.y)/(sa.p2.x - sa.p1.x)
        mb = (sb.p2.y - sb.p1.y)/(sb.p2.x - sb.p1.x)
        x = (ma*sa.p1.x - mb*sb.p1.x + sb.p1.y - sa.p1.y)/(ma - mb)
        y = ma*(x - sa.p1.x) + sa.p1.y
    
    return Point(x, y)



def find_new_event(sl, sr, p):
    pass
    
    
    
    
    
