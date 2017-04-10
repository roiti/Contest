# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

H, W, N = map(int, raw_input().split())
A = coll.defaultdict(int) 
for i in xrange(N):
    a, b = map(int, raw_input().split())
    for dx in xrange(-2, 1):
        for dy in xrange(-2, 1):
            if 0 <= a + dx < H - 2 and 0 <= b + dy < W - 2: continue
            A[(a + dx, b + dy)] += 1

ans = [0]*10
for v in A.values():
    ans[v] += 1

for a in ans:
    print a
