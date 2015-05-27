inf = 10**9

N,C,V = [int(raw_input()) for i in range(3)]
S,T,Y,M = [map(int,raw_input().split()) for i in range(4)]
G = [[[] for i in xrange(N)] for j in xrange(N)]
for s,t,y,m in zip(S,T,Y,M): G[s-1][t-1].append([y,m])

dp = [[inf]*(C+1) for i in xrange(N)]
dp[0][C] = 0
for i in xrange(N):
    for j in xrange(i+1,N):
        for y,m in G[i][j]:
            for c in xrange(y,C+1):
                dp[j][c-y] = min(dp[j][c-y], dp[i][c]+m)
ans = min(dp[N-1])
print ans if ans < inf else -1
