import math
def easeIn (t,b,c,d):
    return c-easeOut(d-t, 0, c, d)+b;
def easeOut (t,b,c,d):
    t/=d
    if (t<(1/2.75)):
        return c*(7.5625*t*t)+b;
    elif (t<(2/2.75)):
        t -= (1.5/2.75)
        return c*(7.5625*t*t+.75)+b;
    elif (t<(2.5/2.75)):
        t -= (2.25/2.75)
        return c*(7.5625*t*t+.9375)+b;
    else:
        t -= (2.625/2.75)
        return c*(7.5625*t*t+.984375)+b;
def easeInOut (t,b,c,d):
    if (t<d/2):
        return easeIn(t*2, 0, c, d)*.5+b;
    return easeOut(t*2-d, 0, c, d)*.5+c*.5+b;
def easeOutIn (t,b,c,d):
    if (t<d/2):
        return easeOut(t*2, 0, c, d)*.5+b;
    return easeIn(t*2-d, 0, c, d)*.5+c*.5+b;