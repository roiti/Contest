# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
ans = 0
for i in xrange(N):
    if sum(map(int, raw_input().split())) < 20:
        ans += 1
print ans
