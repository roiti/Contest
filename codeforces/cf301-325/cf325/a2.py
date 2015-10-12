# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
a = map(int, raw_input().split())
ans = 0
home = True
for i in xrange(n - 1):
    if a[i] == 1:
        home = False
    if a[i] == a[i + 1] == 0:
        home = True
    if not home: ans += 1
ans += a[-1]
print ans
