N,W = map(int,raw_input().split())
dp = [0]*(W+1)
for loop in range(N):
    v,w = map(int,raw_input().split())
    dp[w] = max(dp[w],v)
    for i in range(W-w+1):
        if dp[i]:
            dp[i+w] = max(dp[i+w],dp[i]+v)
print max(dp)


