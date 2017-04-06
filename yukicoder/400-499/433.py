# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll
import heapq

N, K = map(int, raw_input().split())
SPU = [map(int, raw_input().split()) for i in xrange(N)]
SPU = [[S, P, U, i] for i, (S, P, U) in enumerate(SPU)]
SPU.sort(key = lambda x: x[1])
SPU.sort(key = lambda x: -x[0])

C = [0]*100005
ans = []
for S, P, U, i in SPU:
    ans.append([10**18*(S + 1) - C[U]*10**8 + 10**7 - P, i])
    C[U] += 1
ans.sort(reverse = True)

for _, i in ans[:K]:
    print i
