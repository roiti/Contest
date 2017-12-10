# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

ans = ""
N = int(raw_input())
for loop in xrange(N):
    a, b, c = raw_input().split()
    if a[0] == "M":
        ans += c[len(c)/2]
    if a[0] == "B":
        ans += c[0]
    if a[0] == "E":
        ans += c[-1]
print ans
