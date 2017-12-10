# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
p = [map(float, raw_input().split()) for i in xrange(N)]
ans = 0
for ele in it.permutations(xrange(N), N):
    w = set(xrange(N))
    k = 1.0
    for e in ele:
        w -= set([e])
        for wi in w:
            k *= p[wi][e]
    ans += k 

print "%.10f" % ans
