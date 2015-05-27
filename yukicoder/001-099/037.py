T = int(raw_input())
N = int(raw_input())
c = map(int,raw_input().split())
v = map(int,raw_input().split())

dp = [0]*(T+1)
for i in xrange(N):
    vi = v[i]
    while vi:
        for j in xrange(T-c[i],-1,-1):
            if dp[j]: dp[j+c[i]] = max(dp[j+c[i]], dp[j]+vi)
        if c[i] <= T: dp[c[i]] = max(dp[c[i]], vi)
        vi /= 2
print max(dp)