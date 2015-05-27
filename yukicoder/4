N = int(raw_input())
W = map(int,raw_input().split())
sw = sum(W)
dp = [0]*(sw+1)

for w in W:
    for i in range(sw+1-w)[::-1]:
        if dp[i]:
            dp[i+w] = 1
    dp[w] = 1
print "possible" if sw%2 == 0 and dp[sw/2] else "impossible"