inf = 2**31
n,m = map(int,raw_input().split())
coins = map(int,raw_input().split())
dp = [inf]*(n+1)
dp[n] = 0
while dp[0] == inf:
    for coin in coins:
        for i in range(n,coin-1,-1):
            if dp[i] < inf:
                dp[i-coin] = min(dp[i-coin],dp[i]+1)
print dp[0]

