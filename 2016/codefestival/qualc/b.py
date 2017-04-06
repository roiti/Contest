# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

K, T = map(int, raw_input().split())
a = map(int, raw_input().split())

A = [[-ai, i] for i, ai in enumerate(a)]
heapq.heapify(A)
ans = 0
b = -1
for i in xrange(K):
    t = heapq.heappop(A)
    if t[1] == b and A:
        u = heapq.heappop(A)
        if u[0] < -1:
            heapq.heappush(A, [u[0] + 1, u[1]])
        b = u[1]
        heapq.heappush(A, t)
    else:
        if t[1] == b:
            ans += 1
        if t[0] < -1:
            heapq.heappush(A, [t[0] + 1, t[1]])
        b = t[1]
print ans
