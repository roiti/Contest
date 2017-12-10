# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def upper_bound(x):
    i = rank = 0
    n = len(S)
    while True:
        if 2*i + 2 < n and S[2*i + 2] <= x:
            i = 2*i + 2
        elif 2*i + 1 < n and S[2*i + 1] <= x:
            i = 2*i + 1
        elif i < n and S[i] > x:
            return i
        else:
            return i + 1
    
N, K = map(int, raw_input().split())
a = [int(raw_input()) - K for i in xrange(N)]

S = []
s = ans = 0
for i in xrange(N):
    s += a[i]
    if s >= 0: ans += 1
    ans += i - upper_bound(-s)
    heapq.heappush(S, s)

print ans
