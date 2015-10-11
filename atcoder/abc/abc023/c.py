# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

R, C, K = map(int, raw_input().split())
N = int(raw_input())
rc = [] 
nr = [0] * R
nc = [0] * C
for loop in xrange(N):
    r, c = map(int, raw_input().split())
    nr[r - 1] += 1
    nc[c - 1] += 1
    rc.append((r - 1, c - 1))

cc = [0] * 100005
for nci in nc:
    cc[nci] += 1

ans = 0
for nri in nr:
    k = K - nri
    if k >= 0:
        ans += cc[k]

for r, c in rc:
    if nr[r] + nc[c] == K:
        ans -= 1
    if nr[r] + nc[c] == K + 1:
        ans += 1
print ans
