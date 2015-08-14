dxy = zip([1,0,-1,0],[0,1,0,-1])
R,C = map(int,raw_input().split())
sy,sx = map(int,raw_input().split())
gy,gx = map(int,raw_input().split())
sx,sy,gx,gy = sx-1,sy-1,gx-1,gy-1
A = [list(raw_input()) for i in xrange(R)]
visited = [[False]*C for i in xrange(R)]
 
que = [[sx,sy,0]]
visited[sy][sx] = True
while que:
    x,y,d = que.pop(0)
    if (x,y) == (gx,gy):
        print d
        break
    for dx,dy in dxy:
        nx,ny = x+dx,y+dy
        if 0 <= nx < C and 0 <= ny < R and A[ny][nx] == "." and not visited[ny][nx]:
            visited[ny][nx] = True
            que.append([nx,ny,d+1])
