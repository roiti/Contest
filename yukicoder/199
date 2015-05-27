import itertools as it
XY = [map(int, raw_input().split()) for i in xrange(5)]
for i, j, k, l in it.permutations(xrange(5), 4):
    (x1,y1), (x2,y2), (x3,y3), (xp,yp) = XY[i], XY[j], XY[k], XY[l]

    def S(x1, y1, x2, y2, x3 = xp, y3 = yp):
        return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0
        
    if S(x1,y1,x2,y2) + S(x1,y1,x3,y3) + S(x3,y3,x2,y2) - S(x1,y1,x2,y2,x3,y3) < 0.0000001:
        print "NO"
        break
else:
    print "YES"