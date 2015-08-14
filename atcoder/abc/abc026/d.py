import math
def f(t):
    t /= 2000.0
    return A * t + B * math.sin(C * t * pi)
    
pi = math.pi
A, B, C = map(int, raw_input().split())
 
dt = 100.0 / C
ans = 0.0
for t in xrange(400000):
    if f(t) < 100 and f(t + dt) > 100:
        l, r = t, t + dt
        while abs(f((r + l) / 2.0) - 100) > 1e-7:
            m = (r + l) / 2.0
            v = f(m)
            if v >= 100:
                r = m
            else:
                l = m
        ans = (r + l) / 2.0 / 2000.0
    if f(t) > 100 and f(t + dt) < 100:
        l, r = t, t + dt
        while abs(f((r + l) / 2.0) - 100) > 1e-7:
            m = (r + l) / 2.0
            v = f(m)
            if v >= 100:
                l = m
            else:
                r = m
        ans = (r + l) / 2.0 / 2000.0
    if ans > 0.0:
        break
print "%.20f" % ans
