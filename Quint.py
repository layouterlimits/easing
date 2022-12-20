import math
def easeIn(t,b,c,d):
    t /= d
    return c*t*t*t*t*t+b
def easeOut(t,b,c,d):
    t=t/d-1
    return c*(t*t*t*t*t+1)+b
def easeInOut(t,b,c,d):
    t /= d/2
    if (t<1):
        return c/2*t*t*t*t*t+b
    t -= 2
    return c/2*(t*t*t*t*t+2)+b
def easeOutIn(t,b,c,d):
    t /= d/2
    t-=1
    return c/2*(t*t*t*t*t+1)+b
