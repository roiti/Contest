# -*- coding: utf-8 -*-
import sys,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
a = map(int, raw_input().split())

ans = tmp = 1
for i in xrange(n - 1):
    if a[i] <= a[i + 1]:
        tmp += 1
    else:
        ans = max(ans, tmp)
        tmp = 1
print max(ans, tmp)
