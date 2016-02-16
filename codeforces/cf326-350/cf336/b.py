# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
c = map(int, raw_input().split())
d = c[::-1]

idx = [0]*n
used = [False]*n
for i in xrange(n):
    j = d.index(c[i])
    while not (not used[j] and d[j] == c[i]): j += 1
    used[j] = True
    idx[i] = j

ans = 1
for i in xrange(n - 1):
    if idx[i] > idx[i + 1]:
        ans += 1
print ans
