while 1:
    t,n = map(int,raw_input().split())
    if t == n == 0: break
    block = []
    for loop in range(n):
        x,y = map(int,raw_input().split())
        block.append((x+100,y+100))
    sx,sy = map(int,raw_input().split())
    sx += 100; sy += 100
    visited = [[False]*200 for _ in range(200)]
    visited[sy][sx] = True
    que = [[sx,sy,t]]
    ans = 1
    while que:
        x,y,tt = que.pop(0)
        if tt == 0: continue
        for dx,dy in zip([1,1,0,-1,-1,0],[0,1,1,0,-1,-1]):
            nx,ny = x+dx,y+dy
            if not visited[ny][nx] and (nx,ny) not in block:
                que.append([nx,ny,tt-1])
                visited[ny][nx] = True
                ans += 1
    print ans

