# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, M = map(int, raw_input().split())
G = [[1]*N for i in xrange(N)]
for i in xrange(M):
    x, y = map(int, raw_input().split())
    G[y - 1][x - 1] = 0

dp = [0] * (1 << N)
dp[0] = 1
for i in xrange(1 << N):
    for j in xrange(N):
        if i&(1 << j): continue
        flag = True
        for k in xrange(N):
            if (i >> k) & 1 and G[k][j] == 0:
                flag = False
                break
        if not flag: continue
        dp[i | 1 << j] += dp[i]
print dp[(1 << N) - 1]
