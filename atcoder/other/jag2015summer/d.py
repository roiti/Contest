# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

inf = 1e8

N, M, K = map(int, raw_input().split())
D = map(int, raw_input().split())
idx = {D[i]:i for i in xrange(M)}
v = [map(int, raw_input().split()) for i in xrange(N)]

mn = [inf] * (1 << M + 1)

que = [[["0"]*M, 0]]
while que:
    mask, cost = que.pop(0)
    print mask
    num = int("".join(mask), 2)
    if cost >= mn[num]: continue
    mn[num] = cost
    for i in xrange(K):
        m = ["1"] * M 
        for j in xrange(M):
            if mask[j] == "1": continue
            if v[D[j] - 1][i] in idx:
               m[idx[v[D[j] - 1][i]]] = "0"
        que.append([m, cost + 1])

print mn[(1 << M) - 1]

#dp = [inf] * (1 << M + 1)
#
#for mask in it.product("01", repeat = M):
#    print mask
#    for i in xrange(K):
#        m = ["1"] * M 
#        for j in xrange(M):
#            if mask[j] == "0": continue
#            if v[D[j] - 1][i] in D_set:
#               m[idx[v[D[j - 1][i]]]] = "0"
#        dp[int("".join(m), 2)] = dp[int("".join(mask), 2)] + 1
#print dp[(1 << M + 1) - 1]

