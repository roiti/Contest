# -*- coding: utf-8 -*-
import sys,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
h = map(int, raw_input().split())

mx = [0] * n
for i in xrange(n - 2, -1, -1):
    mx[i] = max(mx[i + 1], h[i + 1])

ans = [max(0, mx[i] - h[i] + 1) for i in xrange(n)]
print " ".join(map(str, ans))
