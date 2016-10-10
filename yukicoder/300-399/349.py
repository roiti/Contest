# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
d = coll.defaultdict(int)
for i in xrange(N):
    d[raw_input()] += 1
if max(d[v] for v in d) <= (N + 1)/2:
    print "YES"
else:
    print "NO"
