# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, k, d = map(int, raw_input().split())
ans = [[1] * n for i in xrange(d)]
j = 1
for i in xrange(d):
    for l in xrange(j, min(n, j + k - 1)):
        ans[i][l] = l - j + 2
    j += k - 1
    if j > n - 1: break
if j > n - 1:
    for line in ans:
        print " ".join(map(str, line))
else:
    print -1
