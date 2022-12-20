import math
def easeIn (t,b,c,d,s=0):
    if (s==0):
        s = 1.70158
    t/=d
    return c*t*t*((s+1)*t-s)+b
def easeOut (t,b,c,d,s=0):
    if (s==0):
        s = 1.70158
    t=t/d-1
    return c*(t*t*((s+1)*t+s)+1)+b
def easeInOut (t,b,c,d,s=0):
    if (s==0):
        s = 1.70158
    t /= d/2
    s *= 1.525
    if (t<1):
        return c/2*(t*t*((s+1)*t-s))+b
    t-=2
    return c/2*(t*t*((s+1)*t+s)+2)+b
def easeOutIn (t,b,c,d,s=0):
    if (s==0):
        s = 1.70158
    t /= d/2
    s *= 1.525
    if (t<1):
        t-=1
        return c/2*(t*t*((s+1)*t+s)+1)+b
    t-=1
    return c/2*(t*t*((s+1)*t-s)+1)+b
