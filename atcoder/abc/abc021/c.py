inf = 10**9
mod = 10**9+7
N = int(raw_input())
a, b = map(int, raw_input().split())
a, b = a-1, b-1
G = [[0]*N for i in xrange(N)]
M = int(raw_input())
for loop in xrange(M):
    x, y = map(int, raw_input().split())
    x, y = x-1, y-1
    G[x][y] = G[y][x] = 1
    
combs = [0]*N
combs[a] = 1
steps = [inf]*N
steps[a] = 0
que = [a]
while que:
    cur = que.pop(0)
    for nxt in xrange(N):
        if G[cur][nxt] and steps[nxt] > steps[cur]:
            combs[nxt] = (combs[nxt]+combs[cur])%mod
            steps[nxt] = steps[cur]+1
            if nxt not in que: que.append(nxt)
 
print combs[b]%mod
