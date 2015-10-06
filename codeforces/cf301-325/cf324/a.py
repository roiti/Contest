# -*- coding: utf-8 -*-
import sys,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, t = map(int, raw_input().split())
if t < 10:
    print str(t) * n
else:
    if n < 2:
        print -1
    else:
        print "1" + "0" * (n - 1)
