# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
a = [map(int, raw_input().split()) for i in xrange(2)]
b = map(int, raw_input().split())

ans = 1e10
for i in xrange(n):
    for j in xrange(i + 1, n):
        go = sum(a[1][i:]) + b[i] + sum(a[0][:i])
        back = sum(a[1][j:]) + b[j] + sum(a[0][:j])
        ans = min(ans, go + back)
print ans
