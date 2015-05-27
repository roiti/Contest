n,p,t = raw_input().split()
n,p,t = int(n),float(p),int(t)
dp = [[0]*(n+1) for i in xrange(t+1)]
q = 1.-p
for i in xrange(1,t+1):
    for j in xrange(1,n+1):
        dp[i][j] += p * (dp[i-1][j-1]+1) + q * dp[i-1][j]
print "%.7f"%dp[t][n]
