import math
def easeIn(t, b, c, d):
    if t==d:
        return b+c
    if t==0:
        return b
    w = math.sqrt(2 * 9.81)
    x = math.cosh(w * t / d)
    p = x / math.cosh(w)
    eased = b + c * p
    return eased


def easeOut(t, b, c, d):
    if t==d:
        return b+c
    if t==0:
        return b
    w = math.sqrt(2 * 9.81)
    x = math.cosh(w * (d - t) / d)
    p = 1 - x / math.cosh(w)
    eased = b + c * p
    return eased

'''def easeInOut(t, b, c, d):
    if t < d / 2:
        return easeIn(t * 2, b, c / 2, d)
    return b + c / 2 + easeOut(t - d / 2, 0, c / 2, d / 2)

def easeOutIn(t, b, c, d):
    if t < d / 2:
        return easeOut(t * 2, b, c / 2, d)
    return b + c / 2 + easeIn(t - d / 2, 0, c / 2, d / 2)'''
    
def easeInOut(t, b, c, d):
    if t < d / 2:
        return easeIn(t * 2, b, c / 2, d)
    return easeOut((t * 2) - d, b + c / 2, c / 2, d)

def easeOutIn(t, b, c, d):
    if t < d / 2:
        return easeOut(t * 2, b, c / 2, d)
    return easeIn((t * 2) - d, b + c / 2, c / 2, d)
