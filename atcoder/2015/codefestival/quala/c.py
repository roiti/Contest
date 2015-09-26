# -*- coding: utf-8 -*-
import sys,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, T = map(int, raw_input().split())
AB = [map(int, raw_input().split()) for i in xrange(N)]
AB = sorted(AB, key = lambda x: x[0] - x[1])

t = sum(B for A, B in AB)
ans = N
if t > T:
    print -1
else:
    for A, B in AB:
        d = A - B
        t += d
        if t > T:
            break
        ans -= 1
    print ans
