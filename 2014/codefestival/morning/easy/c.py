inf = 0x10101010
 
def dijkstra(s):
    d = [inf]*V
    used = [False]*V
    prev = [-1]*V
    d[s] = 0
    while 1:
        v = -1
        for u in range(V):
            if not used[u] and (v == -1 or d[u] < d[v]):
                v = u
 
        if v == -1: break
        used[v] = True
 
        for u in range(V):
            d[u] = min(d[u],d[v] + G[v][u])
    return d
 
 
n,m = map(int,raw_input().split())
V = n+1
G = [[inf]*V for i in range(V)]
s,t = map(int,raw_input().split())
for roop in range(m):
   x,y,d = map(int,raw_input().split())
   G[x][y] = G[y][x] = d
 
dist1 = dijkstra(s)
dist2 = dijkstra(t)
for mid in range(1,n+1):
    if mid == s or mid == t: continue
    if dist1[mid] == dist2[mid] and dist1[mid] < inf:
        print mid
        break
else:
    print -1
