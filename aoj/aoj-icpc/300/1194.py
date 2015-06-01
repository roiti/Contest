while 1:
    r,n = map(int,raw_input().split())
    if r == 0: break

    h = {i:0 for i in xrange(-21,21)}
    for loop in xrange(n):
        xl,xr,hi = map(int,raw_input().split())
        for i in xrange(xl,xr):
            h[i] = max(h[i],hi)

    for i in xrange(20,-21,-1):
        h[i] = min(h[i-1],h[i])

    y,d,u = 0,-r,h[0]-r
    for loop in xrange(30):
        if any(x**2+(y-h[x])**2 < r**2 for x in xrange(-20,21)):
            u = y
        else:
            d = y
        y = (d+u)/2.
    print "%.4f"%abs(y+r)


