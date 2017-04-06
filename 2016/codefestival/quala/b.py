# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
a = map(int, raw_input().split())

ans = 0
used = [False]*N
for i in xrange(N):
    if not used[i]:
        if a[a[i] - 1] == i + 1 and not used[a[i] - 1]:
            ans += 1
            used[a[i] - 1] = True
print ans
