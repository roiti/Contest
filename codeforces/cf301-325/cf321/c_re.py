# -*- coding: utf-8 -*-
import sys,math,heapq,itertools as it,fractions,re,bisect,collections as coll
sys.setrecursionlimit(1000000)

def solve(i, c):
    used[i] = True
    if a[i]: c += 1
    else: c = 0
    if c > m: return 0
    res = 0
    leaf = True
    for j in edge[i]:
        if used[j]: continue 
        res += solve(j, c)
        leaf = False
    if leaf: return 1
    return res

n, m = map(int, raw_input().split())
a = map(int, raw_input().split())
edge = [[] for i in xrange(n)]
for loop in xrange(n - 1):
    x, y = map(int, raw_input().split())
    edge[x - 1].append(y - 1)
    edge[y - 1].append(x - 1)

used = [False] * n
print solve(0, 0)
