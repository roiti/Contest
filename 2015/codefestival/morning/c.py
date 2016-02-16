# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, K, M, R = map(int, raw_input().split())
S = sorted([int(raw_input()) for i in xrange(N - 1)], reverse = True)
if sum(S[:K]) < K*R:
    A = K*R - sum(S[:K - 1])
    print A if A <= M else -1
else:
    print 0

