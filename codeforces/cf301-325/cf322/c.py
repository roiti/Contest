# -*- coding: utf-8 -*-
import sys,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, k = map(int, raw_input().split())
a = map(int, raw_input().split())
a = sorted(a, key = lambda ai:(ai + 10) / 10 * 10 - ai)

for i in xrange(n):
    if a[i] < 100:
        need = (a[i] + 10) / 10 * 10 - a[i]
        if k >= need:
            k -= need
            a[i] += need

ans = 0
a = sorted(a, key = lambda ai:(ai + 10) / 10 * 10 - ai)
for i in xrange(n):
    d = 100 - a[i]
    ans += (a[i] + min(d, k)) / 10
    k = max(0, k - d)
print ans
