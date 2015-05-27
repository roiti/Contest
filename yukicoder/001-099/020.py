from collections import deque
dxy = zip([1,0,-1,0],[0,1,0,-1])
def bfs(que):
    while que:
        x,y,v = que.popleft()
        if (x,y) == (N-1,N-1): return True
        if HP[y][x] > v: continue
        HP[y][x] = v
        for dx,dy in dxy:
            nx,ny = x+dx,y+dy
            if 0 <= nx < N and 0 <= ny < N and v-L[ny][nx] >  HP[ny][nx]:
                HP[ny][nx] = v-L[ny][nx]
                que.append([nx,ny,v-L[ny][nx]])
    return False
    
N,V,Ox,Oy = map(int,raw_input().split())
L = [map(int,raw_input().split()) for i in xrange(N)]
HP = [[0]*N for i in xrange(N)]
if bfs(deque([[0,0,V]])): print "YES"
else:
    V = 2*HP[Oy-1][Ox-1]
    HP = [[0]*N for i in xrange(N)]
    if bfs(deque([[Ox-1,Oy-1,V]])): print "YES"
    else: print "NO"