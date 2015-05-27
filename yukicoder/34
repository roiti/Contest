dxy = zip([1,0,-1,0],[0,1,0,-1])
N,V,Sx,Sy,Gx,Gy = map(int,raw_input().split())
Sx,Sy,Gx,Gy = Sx-1,Sy-1,Gx-1,Gy-1
L = [map(int,raw_input().split()) for i in xrange(N)]
HP = [[0]*N for i in xrange(N)]
que = [[Sx,Sy,V,0]]
while que:
    x,y,v,d = que.pop(0)
    if (x,y) == (Gx,Gy):
        print d
        break
    if HP[y][x] > v: continue
    HP[y][x] = v
    for dx,dy in dxy:
        nx,ny = x+dx,y+dy
        if 0 <= nx < N and 0 <= ny < N and v-L[ny][nx] > HP[ny][nx]:
            HP[ny][nx] = v-L[ny][nx]
            que.append([nx,ny,v-L[ny][nx],d+1])
else:
    print -1
