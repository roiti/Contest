# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

a1, b1 = sorted(map(int, raw_input().split()))
a2, b2 = map(int, raw_input().split())
a3, b3 = map(int, raw_input().split())

for loop in xrange(2):
    ax, bx = sorted([max(a2, a3), b2 + b3])
    ay, by = sorted([max(a2, b3), b2 + a3])
    if (ax <= a1 and bx <= b1) or (ay <= a1 and by <= b1):
        print "YES"
        break
    a2, b2 = b2, a2
else:
    print "NO"

