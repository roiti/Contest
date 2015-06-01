inf = 10**9

while 1:
    W,H = map(int,raw_input().split())
    if W == 0: break
    S = [map(int,raw_input().split()) for i in xrange(H)]
    c = map(int,raw_input().split())

    costs = [[[[inf]*W for i in xrange(H)] for j in xrange(3)] for k in xrange(3)]
    costs[2][0][0][0] = 0
    que = [[0,0,1,0,0]]
    while que:
        w,h,dw,dh,cost = que.pop(0)
        if (w,h) == (W-1,H-1): continue
        if costs[dw+1][dh+1][h][w] < cost: continue

        dxy = [(dw,dh),(-dh,dw),(-dw,-dh),(dh,-dw)]

        for i in xrange(4):
            dx,dy = dxy[i]
            nw,nh = w+dx,h+dy
            if 0 <= nw < W and 0 <= nh < H:
                ncost = cost+bool(i != S[h][w])*c[i]
                if costs[dx+1][dy+1][nh][nw] <= ncost: continue
                costs[dx+1][dy+1][nh][nw] = ncost
                que.append([nw,nh,dx,dy,ncost])
    print min(min(costs[i][j][H-1][W-1] for i in xrange(3)) for j in xrange(3))
        


