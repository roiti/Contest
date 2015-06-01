import sys
sys.setrecursionlimit(3000)
def rec(x,y,c):
    if   A[y][x] == ".": A[y][x] = c
    elif A[y][x] != c  : A[y][x] = "x"
    for dx,dy in zip([1,0,-1,0],[0,1,0,-1]):
        nx,ny = x+dx,y+dy
        if 0 <= nx < w and 0 <= ny < h and A[ny][nx] in [".","b" if c == "w" else "w"]:
            rec(nx,ny,c)

while 1:
    w,h = map(int,raw_input().split())
    if w == 0: break
    A = [list(raw_input()) for _ in range(h)]
    for y in range(h):
        for x in range(w):
            if A[y][x] == "W": rec(x,y,"w")
            if A[y][x] == "B": rec(x,y,"b")
    print sum(Ai.count("b") for Ai in A),sum(Ai.count("w") for Ai in A)

