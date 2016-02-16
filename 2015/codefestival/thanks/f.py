# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
cnt = 0
for i in xrange(N - 1):
    a, b = map(int, raw_input().split())
    if a != 1 and b != 1:
        cnt += 1
    else:
        cnt -= 1
cnt = max(0, cnt)
print "A" if cnt%2 else "B"
