inf = 1 << 28
def calc(xyzr1,xyzr2):
    x1,y1,z1,r1 = xyzr1
    x2,y2,z2,r2 = xyzr2
    d = ((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)**0.5
    return max(0, d-r1-r2)
    
while 1:
    n = int(raw_input())
    if n == 0: break
    xyzr = [map(float,raw_input().split()) for i in xrange(n)]
    
    cost = [[0]*n for i in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            cost[i][j] = cost[j][i] = calc(xyzr[i],xyzr[j])
    
    mincost = [inf]*n
    used = [False]*n
    mincost[0] = 0
    ans = 0
    while 1:
        v = -1
        for u in xrange(n):
            if not used[u] and (v == -1 or mincost[u] < mincost[v]): v = u
        if v == -1: break
        used[v] = True
        ans += mincost[v]
        for u in xrange(n):
            mincost[u] = min(mincost[u], cost[v][u])
    
    print "%.3f"%ans
    
    

