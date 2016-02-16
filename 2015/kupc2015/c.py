# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

inf = 1e12
T = int(raw_input())
for loop in xrange(T):
    N = int(raw_input())
    a = [map(int, raw_input().split()) for i in xrange(N)]

    b = copy.deepcopy(a)
    for i in xrange(N):
        b[i][i] = 0
        for j in xrange(N):
            if b[i][j] == -1:
                b[i][j] = inf
    for k in xrange(N):
        for i in xrange(N):
            for j in xrange(N):
                b[i][j] = min(b[i][j], b[i][k] + b[k][j])
    for i in xrange(N):
        for j in xrange(N):
            if b[i][j] >= inf:
                b[i][j] = -1
    print "YES" if a == b else "NO"
