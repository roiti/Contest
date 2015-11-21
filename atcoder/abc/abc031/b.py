# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

L, H = map(int, raw_input().split())
N = int(raw_input())
for i in xrange(N):
    A = int(raw_input())
    if A > H:
        print -1
    elif L <= A <= H:
        print 0
    else:
        print L - A
