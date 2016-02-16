# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

h1, m1 = map(int, raw_input().split())
hn, mn = map(int, raw_input().split())
m1 = 60*h1 + m1
mx = 60*hn + mn
for mt in xrange(mx, 12*60):
    if mt <= m1:
        print "Yes"
        break
    h = mt/60
    m = mt%60
    my = ((h+6)%12)*60 + (m+30)%60
    if my <= m1:
        print "Yes"
        break
else:
    print "No"
