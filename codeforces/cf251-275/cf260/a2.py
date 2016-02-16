# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
for loop in xrange(n):
    a, b = map(int, raw_input().split())
    if a < b:
        print "Happy Alex"
        break
else:
    print "Poor Alex"
