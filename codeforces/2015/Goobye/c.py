# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll


h, w = map(int, raw_input().split())
A = [raw_input() for i in xrange(h)]
q = int(raw_input())
for loop in xrange(q):
    r1, c1, r2, c2 = map(int, raw_input().split())
