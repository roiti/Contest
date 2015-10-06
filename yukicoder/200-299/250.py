dp = [1] * 3001
for i in xrange(3000):
    dp[i + 1] = (i + 1) * dp[i]

Q = int(raw_input())
for loop in xrange(Q):
    D, X, T = map(int, raw_input().split())
    print "AC" if dp[X + D - 1] / dp[X] / dp[D - 1] <= T else "ZETUBOU"
