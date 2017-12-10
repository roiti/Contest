# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(input())
S = []
for i in range(N):
    S.append(input())
a = input().strip()
_ = input()
tmp = input()
b, c = tmp[0], tmp[4] 
_ = input()
d = input().strip()

sa, sb, sc, sd = set(), set(), set(), set()
for s in S:
    if s.startswith(a):
        sa.add(s[1])
for s in S:
    if s.endswith(b):
        sb.add(s[0])
for s in S:
    if s.endswith(c):
        sc.add(s[0])
for s in S:
    if s.endswith(d):
        sd.add(s[0])
ans = list(sa & sb & sc & sd)[0]
print(ans)
