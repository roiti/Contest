# -*- coding: utf-8 -*-
import sys,math,heapq,itertools as it,fractions,re,bisect,collections as coll

T = int(raw_input())
for loop in xrange(T):
    N = int(raw_input())
    A = map(int, raw_input().split())
    ans = 0
    tmp = 1
    for i in xrange(N - 1):
        if A[i] <= A[i + 1]:
            tmp += 1
        else:
            ans += tmp * (tmp + 1) / 2
            tmp = 1
    ans += tmp * (tmp + 1) / 2
    print ans 
