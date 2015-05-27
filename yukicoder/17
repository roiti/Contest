inf = 1 << 28

N = int(raw_input())
S = [int(raw_input()) for i in xrange(N)]
M = int(raw_input())
d = [[inf]*N for i in xrange(N)]
for i in xrange(N): d[i][i] = 0
for loop in xrange(M):
    A,B,C = map(int,raw_input().split())
    d[A][B] = d[B][A] = C
    
for k in xrange(N):
    for i in xrange(N):
        for j in xrange(N):
            d[i][j] = min(d[i][j], d[i][k]+d[k][j])
ans = inf
for i in xrange(1,N-1):
    for j in xrange(1,N-1):
        if i == j: continue
        cost = S[i]+S[j]+d[0][i]+d[i][j]+d[j][N-1]
        ans = min(ans, cost)
print ans