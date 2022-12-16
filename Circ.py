import math
def easeIn (t,b,c,d):
    t/=d
    return -c*(math.sqrt(1-t*t)-1)+b;
def easeOut (t,b,c,d):
    t=t/d-1
    return c*math.sqrt(1-t*t)+b;
def easeInOut (t,b,c,d):
    t/=d/2
    if (t<1):
        return -c/2*(math.sqrt(1-t*t)-1)+b;
    t-=2
    return c/2*(math.sqrt(1-t*t)+1)+b;
def easeOutIn (t,b,c,d):
    t/=d/2
    if (t<1):
        t-=1
        return c/2*math.sqrt(1-t*t)+b;
    t-=1
    return c/2*(2-math.sqrt(1-t*t))+b;