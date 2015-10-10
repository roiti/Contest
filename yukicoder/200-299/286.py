inf  =1e10
N = int(raw_input())
M = [int(raw_input()) for i in xrange(N)]
s = [0] * (1 << N)
for i in xrange(1 << N):
    s[i] = sum(M[j] for j in xrange(N) if (i >> j) & 1)

dp = [inf] * (1 << N)
dp[0] = 0

for mask in xrange(1 << N):
    for i in xrange(N):
        if not (mask >> i) & 1:
            dp[mask | (1 << i)] = min(dp[mask | (1 << i)], dp[mask] + max(0, M[i] - s[mask] % 1000))

print dp[(1 << N) - 1]

