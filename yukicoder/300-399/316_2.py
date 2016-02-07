# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
a, b, c = map(int, raw_input().split())
ans = set()
for i in xrange(1, 1000000):
    if a*i > N: break
    ans.add(a*i)
for i in xrange(1, 1000000):
    if b*i > N: break
    ans.add(b*i)
for i in xrange(1, 1000000):
    if c*i > N: break
    ans.add(c*i)

print len(ans)
