# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, m = map(int, raw_input().split())
s = set()
for loop in xrange(n):
    s |= set(map(int, raw_input().split())[1:])
print "YES" if len(s) == m else "NO"
