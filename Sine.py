import math
def easeIn (t,b,c,d):
    return -c*math.cos(t/d*(math.pi/2))+c+b
def easeOut (t,b,c,d):
    return c*math.sin(t/d*(math.pi/2))+b
def easeInOut (t,b,c,d):
    return -c/2*(math.cos(math.pi*t/d)-1)+b
def easeOutIn (t,b,c,d):
    t/=(d/2)
    if (t<1):
        return c/2*(math.sin(math.pi*t/2))+b
    else:
        t-=1
        return -c/2*(math.cos(math.pi*t/2)-2)+b