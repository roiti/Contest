# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

m, n = map(float, raw_input().split())
ans = 0
for i in xrange(1, int(m) + 1):
    ans += 1.0 * i * ((i/m)**n - ((i - 1)/m)**n)
print "%.10f" % ans
