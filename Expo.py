import math
def easeIn (t,b,c,d):
    if (t == 0):
        return b;
    if (t == d):
        return b + c;
    return  c*math.pow(2, 10*(t/d-1))+b;
def easeOut (t,b,c,d):
    if (t == 0):
        return b;
    if (t == d):
        return b + c;
    return c*(-math.pow(2, -10*t/d)+1)+b;
def easeInOut (t,b,c,d):
    if (t == 0):
        return b;
    if (t == d):
        return b+c;
    t/=(d/2)
    if (t<1):
        return c/2*math.pow(2, 10*(t-1))+b;
    t-=1
    return c/2*(-math.pow(2, -10*t)+2)+b;
def easeOutIn (t,b,c,d):
    if (t == 0):
        return b;
    if (t == d):
        return b+c;
    t/=(d/2)
    if (t<1):
        return c/2*(-math.pow(2, -10*t)+1)+b;
    return c/2*(math.pow(2, 10*(t-2))+1)+b;
