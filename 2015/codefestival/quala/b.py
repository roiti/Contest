# -*- coding: utf-8 -*-
import sys,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
A = map(int, raw_input().split())

ans = 0
for i, a in enumerate(A):
    ans += 2 ** (N - i - 1) * a

print ans
