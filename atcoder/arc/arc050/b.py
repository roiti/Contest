# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll
 
def f(a):
    return a + min(R - x*a, (B - a)/y) if a >= 0 and R - x*a >= 0 and B - a >= 0 else -1
 
R, B = map(int, raw_input().split())
x, y = map(int, raw_input().split())
 
lo, hi = 0, min(R/x, B)
while hi - lo > 0:
    lm = (2*lo + hi)/3
    hm = (lo + 2*hi)/3
    lb = min(R - x*lm, (B - lm)/y)
    hb = min(R - x*hm, (B - hm)/y)
 
    if lm + lb > hm + hb:
        hi = hm - 1
    else:
        lo = lm + 1
 
print max(f(hi + i) for i in xrange(-10, 10))
