# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, v = map(int, raw_input().split())
ans = []
for i in xrange(n):
    s = map(int, raw_input().split())[1:]
    for si in s:
        if si < v:
            ans.append(i + 1)
            break
print len(ans)
print " ".join(map(str, ans))

