dxy = zip([1,0,-1,0],[0,1,0,-1])
def rec(x,y,t):
    global ans
    if t >= ans: return
    for dx,dy in dxy:
        nx,ny = x+dx,y+dy
        while 0 <= nx < W and 0 <= ny < H:
            if   field[ny][nx] == 3: ans = t
            elif field[ny][nx] == 1:
                if abs(nx-x)+abs(ny-y) == 1: break
                field[ny][nx] = 0
                rec(nx-dx,ny-dy,t+1)
                field[ny][nx] = 1
                break
            nx += dx; ny += dy

while 1:
    W,H = map(int,raw_input().split())
    if W == 0: break
    field = [map(int,raw_input().split()) for _ in range(H)]
    for y in range(H):
        for x in range(W):
            if field[y][x] == 2: sx,sy = x,y
    ans = 11
    rec(sx,sy,1)
    print ans if ans < 11 else -1

