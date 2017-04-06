# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, K = map(int, raw_input().split())
s = [int(raw_input()) for i in xrange(N)]

if 0 in s:
    print N
    exit()

ans = 0
j = 0
k = s[0]
for i in xrange(N):
    while k <= K:
        ans = max(ans, j - i + 1)
        j += 1
        if j >= N: break
        k *= s[j]
    else:
        if s[i] > k: continue
        k /= s[i]

    if j >= N: break

print ans
