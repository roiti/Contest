import copy
inf = 10**9
N,M,S,G = map(int,raw_input().split())
cost = [[inf]*N for i in xrange(N)]
for i in xrange(N): cost[i][i] = 0
for loop in xrange(M):
    a,b,c = map(int,raw_input().split())
    cost[a][b] = cost[b][a] = c

mincost = copy.deepcopy(cost)
for k in xrange(N):
    for i in xrange(N):
        for j in xrange(N):
            mincost[i][j] = min(mincost[i][j], mincost[i][k]+mincost[k][j])

ans = [S]
while S != G:
    for i in xrange(N):
        if i != S and cost[S][i]+mincost[i][G] == mincost[S][G]:
            ans.append(i)
            S = i
            break
print " ".join(map(str,ans))

