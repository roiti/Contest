# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def dfs(x, y):
    if x == y == 0: return True
    k = min(x, y)
    if k == 0: k = max(x, y)
    res = False
    for d in (max(1, k - 3), k + 1):
        if x - d >= 0: res |= not dfs(x - d, y)
        if y - d >= 0: res |= not dfs(x, y - d)
    return res
X, Y = map(int, raw_input().split())
print "snuke" if dfs(X, Y) else "rng"

