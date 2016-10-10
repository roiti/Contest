# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

A = int(raw_input())
for i in xrange(7, A):
    if A - i == 7:
        print i
        break
else:
    print -1
