# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
A = map(int, raw_input().split())

B = [[] for i in xrange(100005)]
for i in xrange(N): B[A[i]].append(i)

ans = 0
i = 0
for b in B:
    if not b: continue
    if b[0] < i:
        ans += 1
        i = b[bisect.bisect(b, i) - 1]
    else:
        i = b[-1]
if A[0] == max(A): ans = max(0, ans - 1)

print ans + 1 
