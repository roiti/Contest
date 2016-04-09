# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
a = [int(raw_input()) for i in xrange(N)]

q = []
for i, ai in enumerate(a):
    heapq.heappush(q, [ai, i])

b = [0] * N
mn = min(a)
rank = 0
while q:
    ai, i = heapq.heappop(q)
    if ai > mn:
        mn = ai
        rank += 1
    b[i] = rank

for bi in b:
    print bi
