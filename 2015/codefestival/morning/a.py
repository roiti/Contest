# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
for i in xrange(100000):
    if int((N + i)**0.5) ** 2 == N + i:
        print i
        break
