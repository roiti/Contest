# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

T = int(raw_input())
for loop in xrange(T):
    N, D = map(int, raw_input().split())
    ans = 0
    for i in xrange(N - 2):
        ans += 127
        D ^= 127

    mx = 0
    if N > 1:
        for i in xrange(1, 128):
            mx = max(mx, i + (D^i))
        print ans + mx
    else:
        print D

