# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

T = int(raw_input())
for loop in xrange(T):
    n, m = map(int, raw_input().split())
    uv = [map(int, raw_input().split()) for i in xrange(m)]
    print "yes" if (n - 2*m)%2 == 0 else "no"
