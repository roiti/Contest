# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
b = map(int, raw_input().split())
b.sort()

if b[0] != b[-1]:
    print b[-1] - b[0], b.count(b[0]) * b.count(b[-1])
else:
    print 0, n * (n - 1) / 2

