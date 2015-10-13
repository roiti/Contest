# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
a = map(int, raw_input().split())
goal = range(n)

for i in xrange(n):
    for j in xrange(n):
        if j % 2 == 0:
            a[j] = (a[j] + 1) % n
        else:
            a[j] = (a[j] - 1 + n) % n
    if a == goal:
        print "Yes"
        break
else:
    print "No"
