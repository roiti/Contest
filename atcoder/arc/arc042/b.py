import math
def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) 
    
x0, y0 = map(int, raw_input().split())
N = int(raw_input())
xy = [map(int, raw_input().split()) for i in xrange(N)]
 
ans = 1e9
for i in xrange(N):
    x1, y1 = xy[i]
    x2, y2 = xy[(i + 1) % N]
    for loop in xrange(100):
        lx, ly = (2 * x1 + x2) / 3.0, (2 * y1 + y2) / 3.0
        rx, ry = (x1 + 2 * x2) / 3.0, (y1 + 2 * y2) / 3.0
        ld, rd = dist(lx, ly, x0, y0), dist(rx, ry, x0, y0)
        if ld < rd:
            ans = min(ans, ld)
            x2, y2 = rx, ry
        else:
            ans = min(ans, rd)
            x1, y1 = lx, ly
print "%.10f" % ans
