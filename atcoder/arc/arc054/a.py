# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll
 
L, X, Y, S, D = map(int, raw_input().split())
 
ans = 0
if D >= S:
    if X >= Y:
        ans = 1.0*(D - S)/(X + Y)
    else:
        ans = min(1.0*(D - S)/(X + Y), 1.0*(S + L - D)/(Y - X))
else:
    if X >= Y:
        ans = 1.0*(L - S + D)/(X + Y) 
    else:
        ans = min(1.0*(L - S + D)/(X + Y), 1.0*(S - D)/(Y - X))
 
print "%.10f" % ans
