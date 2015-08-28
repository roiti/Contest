mod = 10 ** 9 + 7
N, S, K = map(int, raw_input().split())

dp = [[0] * (S + 1) for i in xrange(N)]
dp[0][0] = 1
for i in xrange(1, N):
    


print sum(dp[N - 1][:S + 1]) % mod
