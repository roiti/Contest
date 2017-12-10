# -*- coding: utf-8 -*-

def rem(i, j, k, mod):
    return 1 if (i + 2*j + 3*k) % mod == 0 else 0

T = int(raw_input())

for case in xrange(1, T + 1):
    N, P = map(int, raw_input().split())
    G = map(int, raw_input().split())
    r = [0]*4
    for Gi in G:
        r[Gi%P] += 1

    dp = [[[0]*105 for i in xrange(105)] for i in xrange(105)]
    for i in xrange(r[1] + 1):
        for j in xrange(r[2] + 1):
            for k in xrange(r[3] + 1):
                if i > 0:
                    dp[i][j][k] = max(dp[i - 1][j][k] + rem(i - 1, j, k, P), dp[i][j][k])
                if j > 0:
                    dp[i][j][k] = max(dp[i][j - 1][k] + rem(i, j - 1, k, P), dp[i][j][k])
                if k > 0:
                    dp[i][j][k] = max(dp[i][j][k - 1] + rem(i, j, k - 1, P), dp[i][j][k])

    ans = dp[r[1]][r[2]][r[3]] + r[0]
    print "Case #%d: %d" % (case, ans)

