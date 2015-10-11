# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
T = int(raw_input())
A = map(int, raw_input().split())
dp = [[False] * (T + 10) for i in xrange(N + 1)]
dp[N][T] = True

for i in xrange(N - 1, -1, -1):
    for j in xrange(T + 1):
        if j + A[i] <= T and dp[i + 1][j + A[i]]:
            dp[i][j] = True
        if j * A[i] <= T and dp[i + 1][j * A[i]]:
            dp[i][j] = True

ans = "";
c = A[0];
for i in xrange(1, N):
    if dp[i + 1][c + A[i]]:
        ans += "+"
        c += A[i]
    else:
        ans += "*"
        c *= A[i]
print ans
