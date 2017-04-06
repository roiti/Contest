# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

inf = 1e10
def gcd(a, b):
    while b: a, b = b, a%b
    return a

N, Ma, Mb = map(int, raw_input().split())
abc = [map(int, raw_input().split()) for i in xrange(N)]

dp = [[0]*405 for i in xrange(405)]

for a, b, c in abc:
    for i in xrange(404-a, -1, -1):
        for j in xrange(404-b, -1, -1):
            if dp[i][j]:
                if dp[i + a][j + b] == 0: dp[i + a][j + b] = dp[i][j] + c
                else: dp[i + a][j + b] = min(dp[i + a][j + b], dp[i][j] + c)
    if dp[a][b] == 0: dp[a][b] = c
    else: dp[a][b] = min(dp[a][b], c)

ans = inf
for i in xrange(1, 405):
    for j in xrange(1, 405):
        g = gcd(i, j)
        if i/g == Ma and j/g == Mb and dp[i][j]:
            ans = min(ans, dp[i][j])

print ans if ans < inf else -1
