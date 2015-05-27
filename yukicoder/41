mod = 10**9+9
mx = 100000
dp = [1]*mx
for i in xrange(1,10):
    for j in xrange(i,mx):
        dp[j] = (dp[j] + dp[j-i])%mod

T = int(raw_input())
for loop in xrange(T):
    M = int(raw_input())
    M /= 111111
    print dp[M]
