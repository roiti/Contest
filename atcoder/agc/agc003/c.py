# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
A = [int(raw_input()) for i in xrange(N)]

B = sorted(A)
X = set([A[i] for i in xrange(N) if i%2 == 0])
Y = set([B[i] for i in xrange(N) if i%2 == 0])

print len(Y - X)
