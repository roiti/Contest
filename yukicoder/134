def cost(S, v, u):
    s = 0.0
    for i in xrange(N):
        if S >> i & 1 == 0: s += W[i]
    return d[v][u]*(100.0+s)/120.0
    
def rec(S, v):
    if dp[S][v] >= 0.0: return dp[S][v]
    if S == (1 << N)-1:
        dp[S][v] = (abs(x-X[v])+abs(y-Y[v]))*100.0/120.0
        return dp[S][v]

    res = 10**10
    for u in xrange(N):
        if S >> u & 1 == 0:
            res = min(res, rec(S|1 << u, u)+W[u]+cost(S, v, u))
    dp[S][v] = res
    return res

x,y = map(int,raw_input().split())
N = int(raw_input())
X,Y,W = [],[],[]
for loop in xrange(N):
    a,b,c = map(float,raw_input().split())
    X.append(a); Y.append(b); W.append(c)
sumW = sum(W)

d = [[0]*N for _ in xrange(N)]
for i in xrange(N):
    for j in xrange(i+1,N):
        d[i][j] = d[j][i] = abs(X[i]-X[j])+abs(Y[i]-Y[j])
        
ans = 10**10
for s in xrange(N):
    dp = [[-1.0]*N for _ in xrange(2**N)]
    start = (abs(x-X[s])+abs(y-Y[s]))*(100.0+sumW)/120.0+W[s]
    ans = min(ans, rec(1 << s, s)+start)

print ans