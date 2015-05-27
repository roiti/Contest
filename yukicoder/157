dxy = zip([1,0,-1,0],[0,1,0,-1])
def rec(x,y,cnt):
    C[y][x] = str(cnt)
    for dx,dy in dxy:
        nx,ny = x+dx,y+dy
        if 0 <= nx < W and 0 <= ny < H and C[ny][nx] == ".":
            rec(nx,ny,cnt)
            
W,H = map(int,raw_input().split())
C = [list(raw_input()) for i in xrange(H)]
cnt = 0
for y in xrange(H):
    for x in xrange(W):
        if C[y][x] == ".":
            rec(x,y,cnt)
            cnt += 1
ans = 100000
for y1 in xrange(H):
    for x1 in xrange(W):
        for y2 in xrange(H):
            for x2 in xrange(W):
                if C[y1][x1] == "0" and C[y2][x2] == "1":
                    ans = min(ans, abs(x1-x2)+abs(y1-y2))
print ans-1
