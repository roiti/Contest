# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
S = list(raw_input())

if N%2:
    print -1
else:
    ans = 0
    for i in xrange(N/2):
        if S[i] != S[N/2 + i]:
            S[N/2 + i] = S[i]
            ans += 1
    print ans
