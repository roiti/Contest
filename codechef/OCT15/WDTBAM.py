# -*- coding: utf-8 -*-
import sys,math,heapq,itertools as it,fractions,re,bisect,collections as coll

T = int(raw_input())
for loop in xrange(T):
    N = int(raw_input())
    A = raw_input()
    B = raw_input()
    W = map(int, raw_input().split())
    cnt = 0
    for a, b in zip(A, B):
        if a == b:
            cnt += 1
    if cnt == N:
        print W[cnt]
    else:
        print max(W[:cnt + 1])

