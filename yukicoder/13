import sys
sys.setrecursionlimit(100000)
dxy = zip([1,0,-1,0],[0,1,0,-1])
def dfs(x,y,c):
    A[y][x]  = -c
    res = False
    cnt = 0
    for dx,dy in dxy:
        nx,ny = x+dx,y+dy
        if 0 <= nx < W and 0 <= ny < H:
            if A[ny][nx] == c:
                res |= dfs(nx,ny,c)
            elif A[ny][nx] == -c:
                cnt += 1
    return res or cnt > 1
            
W,H = map(int,raw_input().split())
A = [map(int,raw_input().split()) for i in xrange(H)]
ans = False
for y in xrange(H):
    for x in xrange(W):
        if A[y][x] > 0:
            ans |= dfs(x,y,A[y][x])
print "possible" if ans else "impossible"