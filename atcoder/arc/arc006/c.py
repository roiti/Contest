# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
a = []
for i in xrange(N):
    w = int(raw_input())
    for j in xrange(len(a)):
        if a[j] >= w:
            a[j] = w
            break
    else:
        a.append(w)
    a = sorted(a)
print len(a)
