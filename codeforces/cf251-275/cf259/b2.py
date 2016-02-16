# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
a = map(int, raw_input().split())

for i in xrange(n - 1):
    if a[i] > a[i + 1]:
        j = i + 1
        break
else:
    print 0
    exit()

for i in xrange(j, n - 1):
    if a[i] > a[0] or a[i] > a[i + 1]:
        print -1
        exit()
print n - j if a[-1] <= a[0] else -1
