# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
x = sorted(map(int, raw_input().split()))
if len(set(x)) == N and len(set((x[i + 1] - x[i] for i in xrange(N - 1)))) == 1:
    print "YES"
else:
    print "NO"

