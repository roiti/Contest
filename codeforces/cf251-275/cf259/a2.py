# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
ans = [["*"] * n for i in xrange(n)]

for y in xrange(n):
    k = min(2 * y + 1, 2 * (n - y - 1) + 1)
    for x in xrange(k):
        ans[y][x + (n - k)/2] = "D"

for line in ans:
    print "".join(line)
