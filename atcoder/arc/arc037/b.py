# Union Find
par = [0]*110
rank = [0]*110
def init_union_find(V):
    for i in xrange(V):
        par[i] = i
        rank[i] = 0
        
def find(x):
    if par[x] == x: return x
    else:
        par[x] = find(par[x])
        return par[x]
    
def unite(x,y):
    x = find(x)
    y = find(y)
    if (x == y): return
    
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if(rank[x] == rank[y]): rank[x] += 1
 
def same(x,y):
    return find(x) == find(y)
 
N, M = map(int, raw_input().split())
init_union_find(110)
edge = [0]*110
uv = [map(int, raw_input().split()) for i in xrange(M)]
for u, v in uv:
    u -= 1; v -= 1
    unite(u, v)
for u, v in uv:
    edge[find(u-1)] += 1
 
node = [0]*110
for i in xrange(N):
    node[find(i)] += 1
 
ans = 0    
for i in xrange(N):
    if node[i] == edge[i] + 1:
        ans += 1
print ans
