# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

a, b = map(int, raw_input().split())
if a <= 0 and b >= 0:
    print "Zero"
else:
    if a > 0:
        print "Positive"
    else:
        print "Positive" if (b - a) % 2 == 1 else "Negative"
