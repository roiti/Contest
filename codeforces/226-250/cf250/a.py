n,m = map(int,raw_input().split())
v = map(int,raw_input().split())
G = [[0]*n for i in range(n)]
for i in range(m):
    a,b = map(int,raw_input().split())
    G[a-1][b-1] = G[b-1][a-1] = 1

ans = 0
for i,j in sorted(zip(v,range(n)),reverse = True):
    for k in range(n):
        if G[j][k] == 1:
            ans += v[k]
            G[j][k] = G[k][j] = 0
print ans
