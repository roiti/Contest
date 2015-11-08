# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, M = map(int, raw_input().split())
A = map(int, raw_input().split())

cnt = coll.defaultdict(int)
for a in A:
    cnt[a] += 1

for k, v in cnt.items():
    if v > N / 2:
        print k
        break
else:
    print "?"
