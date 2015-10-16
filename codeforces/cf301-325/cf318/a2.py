# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
a = map(int, raw_input().split())
b = a[0]
a = [-a[i] for i in xrange(1, n)]
heapq.heapify(a)
ans = 0
while 1:
    c = -heapq.heappop(a)
    if c < b: break
    ans += 1
    b += 1
    c -= 1
    heapq.heappush(a, -c)
print ans
