# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
SP = [raw_input().split() for i in xrange(N)]
sumP = sum(int(p) for s, p in SP)
for s, p in SP:
    if 2*int(p) > sumP:
        print s
        break
else:
    print "atcoder"
