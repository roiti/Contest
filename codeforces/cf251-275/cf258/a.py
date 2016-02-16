# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, m = map(int, raw_input().split())
if n <= m:
    print "Malvika" if n % 2 == 0 else "Akshat"
else:
    print "Malvika" if m % 2 == 0 else "Akshat"
