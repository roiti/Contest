# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

p, n = map(int, raw_input().split())
used = [False] * p
for i in xrange(n):
    x = int(raw_input())
    if used[x%p]:
        print i + 1
        break
    used[x%p] = True
else:
    print -1

