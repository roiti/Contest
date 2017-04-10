# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll
 
P = float(raw_input())
 
l, r = 0.0, 100 
for loop in xrange(300):
    ml = (2*l + r)/3
    mr = (l + 2*r)/3
    tl = ml + P/(2**(ml/1.5))
    tr = mr + P/(2**(mr/1.5))
    if tl < tr:
        r = mr
    else:
        l = ml
 
print r + P/(2**(r/1.5))
