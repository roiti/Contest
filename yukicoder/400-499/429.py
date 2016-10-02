# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, K, X = map(int, raw_input().split())
P = [raw_input().split() for i in xrange(K)]
C = map(int, raw_input().split())
S = range(1, N + 1)

for i in xrange(X - 1):
    A, B = map(int, P[i])
    S[A - 1], S[B - 1] = S[B - 1], S[A - 1]
for i in xrange(K - 1, X - 1, - 1):
    A, B = map(int, P[i])
    C[A - 1], C[B - 1] = C[B - 1], C[A - 1]

ans = []
for i in xrange(N):
    if S[i] != C[i]:
        ans.append(i + 1)
print ans[0], ans[1] 
