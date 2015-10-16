# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def dfs(a, s, recog, rem):
    if rem == 0:
        if s in edge[a]:
            return recog + len(edge[a])
        else:
            return 1e10
    res = 1e10
    for b in edge[a]:
        if b != a:
            res = min(res,dfs(b, s, recog + len(edge[a]), rem - 1))
    return res

n, m = map(int, raw_input().split())
edge = [[] for i in xrange(n)]
for loop in xrange(m):
    a, b = map(int, raw_input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

ans = 1e10
for i in xrange(n):
    ans = min(ans, dfs(i, i, 0, 2) - 6)

if ans < 1e9:
    print ans
else:
    print -1
