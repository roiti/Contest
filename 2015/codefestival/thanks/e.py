# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

Q = int(raw_input())
for loop in xrange(Q):
    S, T = raw_input().split()
    st = set(T)
    U = ""
    for si in S:
        if si in st:
            U += si
    print "YES" if T in U else "NO"

