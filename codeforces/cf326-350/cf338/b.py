# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, m = map(int, raw_input().split())
branch = [0]*n
seg = [[] for i in xrange(n)]

for loop in xrange(m):
    u, v = map(int, raw_input().split())
    u -= 1
    v -= 1
    branch[u] += 1
    branch[v] += 1
    seg[u].append(v)
    seg[v].append(u)

tail = [1] * n
for i in xrange(n):
    for j in seg[i]:
        if j < i:
            tail[i] = max(tail[i], tail[j] + 1)

print max(tail[i] * branch[i] for i in xrange(n))
