#-*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll
 
A, K = map(int, raw_input().split())
 
ans = 0
if K == 0:
    print 2*10**12 - A
else:
    while A < 2*10**12:
        A = A + 1 + K*A
        ans += 1
    print ans
