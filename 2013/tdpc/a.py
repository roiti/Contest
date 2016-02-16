n = int(raw_input())
p = map(int,raw_input().split())
dp = [0]*10001
dp[0] = 1
for pi in p:
    for j in range(10000-pi,-1,-1):
        if dp[j]:
            dp[j+pi] = 1
print sum(dp)

