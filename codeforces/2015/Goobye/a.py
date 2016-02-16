# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

x, of, z = raw_input().split()
x = int(x)
if z == "week":
    if x <= 4 or x == 7:
        print 52
    else:
        print 53
else:
    if x <= 29:
        print 12
    elif x == 30:
        print 11
    else:
        print 7
