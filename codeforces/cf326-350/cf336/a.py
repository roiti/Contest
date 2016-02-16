# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
ab = [map(int, raw_input().split()) for i in xrange(n)]
ab = sorted(ab)

destroy = [0]*n
ans = n - 1
for i in xrange(1, n):
    a, b = ab[i]
    j = bisect.bisect_left(ab, [a - b, 0])
    destroy[i] = destroy[max(0, j - 1)] + i - j
    ans = min(ans, destroy[i] + n - i - 1)
print ans
