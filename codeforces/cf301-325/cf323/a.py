# -*- coding: utf-8 -*-
import sys,math,heapq,itertools as it,fractions,re,bisect,collections as coll

ans = []
n = int(raw_input())
horizon, verticle = [False] * n, [False] * n
for day in xrange(1, n * n + 1):
    h, v = map(int, raw_input().split())
    if not horizon[h - 1] and not verticle[v - 1]:
        horizon[h - 1] = verticle[v - 1] = True
        ans.append(day)

print " ".join(map(str, ans))

