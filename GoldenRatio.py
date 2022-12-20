def easeIn(t, b, c, d):
    return c * (t / d)**1.61803398875 + b

def easeOut(t, b, c, d):
    return c * (1 - (1 - t / d)**1.61803398875) + b

def easeInOut(t, b, c, d):
    if t < d / 2:
        return easeIn(t * 2, b, c / 2, d)
    return easeOut((t * 2) - d, b + c / 2, c / 2, d)

def easeOutIn(t, b, c, d):
    if t < d / 2:
        return easeOut(t * 2, b, c / 2, d)
    return easeIn((t * 2) - d, b + c / 2, c / 2, d)
