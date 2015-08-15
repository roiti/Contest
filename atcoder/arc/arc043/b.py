mod = 10 ** 9 + 7
MX = 10 ** 5 + 5
N = int(raw_input())
dp = [[0] * MX for i in xrange(4)]
for i in xrange(N):
    d = int(raw_input())
    dp[0][d] += 1
    dp[1][d] += 1
    dp[2][d] += 1
    dp[3][d] += 1

for i in xrange(1, 5):
    for j in xrange(1, MX):
        dp[i - 1][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % mod
    if i == 4: break
    for j in xrange(1, MX):
        dp[i][j] = dp[i][j] * dp[i - 1][j / 2]

print dp[3][-1]
