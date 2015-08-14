inf = 10**12
H,W,T = map(int,raw_input().split())
A = [list(raw_input()) for i in xrange(H)]
for y in xrange(H):
    for x in xrange(W):
        if A[y][x] == "S":
            sx,sy = x,y
        if A[y][x] == "G":
            gx,gy = x,y
            
ans = 0
l,d,r = 1,10**4,10**9+1
for loop in xrange(101):
    G = [[inf]*W for i in xrange(H)]
    G[sy][sx] = 0
    que = [[sx,sy,0]]
    while que:
        x,y,s = que.pop(0)
        for dx,dy in zip([1,0,-1,0],[0,1,0,-1]):
            nx,ny = x+dx,y+dy
            if 0 <= nx < W and 0 <= ny < H:
                if A[ny][nx] == "#":
                    if G[ny][nx] <= s+d:
                        continue
                    G[ny][nx] = s+d
                    que.append([nx,ny,s+d])
                else:
                    if G[ny][nx] <= s+1:
                        continue
                    G[ny][nx] = s+1
                    que.append([nx,ny,s+1])
    if G[gy][gx] <= T:
        ans = max(ans,d)
        l = d
    else:
        r = d
    d = (r+l)/2 if r != l else d+1
print ans
