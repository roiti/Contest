# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
C = map(int, list(raw_input()))
cnt = [0]*4
for c in C:
    cnt[int(c) - 1] += 1

print max(cnt), min(cnt)
