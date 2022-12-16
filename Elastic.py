import math
def easeIn (t,b,c,d,a=0,p=0):
    s=0
    if (t == 0):
        return b
    t/=d
    if (t == 1):
        return b+c
    if (p==0):
        p = d*.3
    if (a==0 or a<math.abs(c)):
        a = c
        s = p/4
    else:
        s = p/(2*math.pi)*math.asin(c/a)
    t -= 1    
    return -(a*math.pow(2, 10*t)*math.sin((t*d-s)*(2*math.pi)/p))+b
def easeOut (t,b,c,d,a=0,p=0):
    s=0
    if (t == 0):
        return b
    t/=d
    if (t == 1):
        return b+c
    if (p==0):
        p = d*.3
    if (a==0 or a<math.abs(c)):
        a = c
        s = p/4
    else:
        s = p/(2*math.pi)*math.asin(c/a)
    return (a*math.pow(2, -10*t)*math.sin((t*d-s)*(2*math.pi)/p)+c+b)
def easeInOut (t,b,c,d,a=0,p=0):
    s=0
    if (t == 0):
        return b
    t /= d/2
    if (t == 2):
        return b+c
    if (p==0):
        p = d*(.3*1.5)
    if (a==0 or a<math.abs(c)):
        a = c
        s = p/4
    else:
        s = p/(2*math.pi)*math.asin(c/a)
    if (t<1):
        t -= 1
        return -.5*(a*math.pow(2, 10*t)*math.sin((t*d-s)*(2*math.pi)/p))+b
    t -= 1
    return a*math.pow(2, -10*t)*math.sin((t*d-s)*(2*math.pi)/p)*.5+c+b
def easeOutIn (t,b,c,d,a=0,p=0):
    s=0
    if (t == 0):
        return b
    t /= d/2
    if (t == 2):
        return b+c
    if (p == 0):
        p = d * (.3 * 1.5)
    if (a==0 or a<math.abs(c)):
        a = c
        s = p/4
    else:
        s = p/(2*math.pi)*math.asin(c/a)
    if (t<1):
        return .5*(a*math.pow(2, -10*t)*math.sin((t*d-s)*(2*math.pi)/p))+c/2+b
    return c/2+.5*(a*math.pow(2, 10*(t-2))*math.sin((t*d-s)*(2*math.pi)/p))+b