# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, K = map(int, raw_input().split())
w, p = [], []
for i in xrange(N):
    wi, pi = map(int, raw_input().split())
    w.append(wi)
    p.append(pi)

wp = [[1.0*p[i]/w[i],i] for i in xrange(N)]
wp = sorted(wp, key = lambda x: x[0], reverse = True)

W, S = 0, 0
for i in xrange(K):
    W += w[i]
    S += p[i] * w[i]

print 1.0*S/W
