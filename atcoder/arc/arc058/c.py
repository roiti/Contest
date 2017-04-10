# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, K = map(int, raw_input().split())
D = set(raw_input().split())
for i in xrange(100000):
    for x in str(N):
        if x in D:
            break
    else:
        print N
        break
    N += 1

