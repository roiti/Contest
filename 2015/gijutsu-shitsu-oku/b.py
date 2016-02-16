# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
a = [[int(raw_input()), i] for i in xrange(N)]
a.sort(reverse = True, key = lambda x:x[0])
print a[0][1] + 1
