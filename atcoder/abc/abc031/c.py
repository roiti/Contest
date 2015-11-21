# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
a = map(int, raw_input().split())

ans = -1e6
for ii in xrange(N):
    chokudai = mx_aoki = -1e6
    for j in xrange(N):
        i = ii
        if i == j: continue
        if i > j: i, j = j, i
        b = a[i:j + 1]
        aoki = sum(b[1::2])
        if aoki > mx_aoki:
            mx_aoki = aoki
            chokudai = sum(b[::2])
    ans = max(ans, chokudai)
print ans
