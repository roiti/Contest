# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

a, b, c, d = map(float, raw_input().split())
x, y = b/a, d/c
if x == y:
    print "DRAW"
elif x < y:
    print "AOKI"
else:
    print "TAKAHASHI"
