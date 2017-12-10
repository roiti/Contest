# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

T = int(raw_input())
for loop in xrange(T):
    N = int(raw_input())
    C = map(int, raw_input().split())
    mn = 1
    seq = 1
    for i in xrange(1, N):
        if C[i] == C[i - 1]:
            seq += 1
        else:
            mn = max(mn, seq)
            seq = 1
    mn = max(mn, seq)
    print "Yes" if mn >= 3 else "No"
