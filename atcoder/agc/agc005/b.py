# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
a = map(int, raw_input().split())

aso = [N]*N
q = [a[0]]
for i in xrange(1, N):
    while q and q[-1] > a[i]:
        aso[q[-1] - 1] = i
        q.pop()
    q.append(a[i])
dso = [-1]*N
q = [a[-1]]
for i in xrange(N - 2, -1, -1):
    while q and q[-1] > a[i]:
        dso[q[-1] - 1] = i 
        q.pop()
    q.append(a[i])

ans = 0
for i in xrange(N):
    ans += a[i] * (aso[a[i] - 1] - i)*(i - dso[a[i] - 1])
print ans
