# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
a = map(int, raw_input().split())

for i in xrange(n - 1):
    if a[i] < 0: break
    if a[i]%2 == 1:
        a[i] = 0
        a[i + 1] -= 1
    else:
        a[i] = 0

if min(a) < 0 or a[n - 1]%2 != 0:
    print "NO"
else:
    print "YES"


