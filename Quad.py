import math
def easeIn (t,b,c,d):
    t/=d
    return c*t*t+b
def easeOut (t,b,c,d):
    t/=d
    return -c*t*(t-2)+b
def easeInOut (t,b,c,d):
    t/=d/2
    if (t<1):
        return c/2*t*t+b
    t-=1
    return -c/2*(t*(t-2)-1)+b
def easeOutIn (t,b,c,d):
    t/=d/2
    if (t < 1):
        t-=1
        return -c/2 * (t*t - 1) + b
    t-=1
    return c/2*(t*t + 1) + b