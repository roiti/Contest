# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

A1, A2 = map(int, raw_input().split())
B1, B2 = map(int, raw_input().split())
C = int(raw_input())

ans = set()
if A1 == C or A2 == C:
    ans.add(B1)
    ans.add(B2)
if B1 == C or B2 == C:
    ans.add(A1)
    ans.add(A2)
ans = sorted(list(ans))
print len(ans)
for i in ans:
    print i
