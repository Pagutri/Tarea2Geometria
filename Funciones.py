from Point import Point

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
