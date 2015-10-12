# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
v, d, p = [], [], []
for loop in xrange(n):
    vi, di, pi = map(int, raw_input().split())
    v.append(vi); d.append(di); p.append(pi)

run = [False] * n
for i in xrange(n):
    if run[i]: continue
    cnt = 0
    for j in xrange(i + 1, n):
        if run[j]: continue
        p[j] -= v[i] - cnt
        cnt += 1
        if cnt == v[i]: break
    for j in xrange(i + 1, n):
        if run[j]: continue
        if p[j] < 0:
            run[j] = True
            for k in xrange(j + 1, n):
                if run[k]: continue
                p[k] -= d[j]

ans = []
for i in xrange(n):
    if not run[i]:
        ans.append(i + 1)
print len(ans)
print " ".join(map(str, ans))
