while 1:
    W,H = map(int,raw_input().split())
    if W == H == 0: break
    wall = [map(int,raw_input().split()) for _ in range(2*H-1)]
    
    dist = [[0]*W for _ in range(H)]
    dist[0][0] = 1
    que = [[0,0]]
    while que:
        x,y = que.pop(0)
        d = dist[y][x]
        for dx,dy in zip([1,0,-1,0],[0,1,0,-1]):
            nx,ny = x+dx, y+dy
            if 0 <= nx < W and 0 <= ny < H:
                if dy == 0:
                    if wall[2*y][min(x,nx)] == 1 or dist[ny][nx] > 0: continue
                if dx == 0:
                    if wall[2*min(y,ny)+1][x] == 1 or dist[ny][nx] > 0: continue
                dist[ny][nx] = d+1
                que.append([nx,ny])
    print dist[-1][-1]                    

