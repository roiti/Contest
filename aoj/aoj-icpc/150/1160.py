import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    C[y][x] = 0
    for dx,dy in zip([1,1,0,-1,-1,-1,0,1],[0,1,1,1,0,-1,-1,-1]):
        if 0 <= x+dx < w and 0 <= y+dy < h and C[y+dy][x+dx] == 1:
            dfs(x+dx, y+dy)

while 1:
    w,h = map(int,raw_input().split())
    if w == h == 0: break
    C = [map(int,raw_input().split()) for _ in xrange(h)]

    ans = 0
    for y in range(h):
        for x in range(w):
            if C[y][x] == 1:
                dfs(x, y)
                ans += 1
    print ans

