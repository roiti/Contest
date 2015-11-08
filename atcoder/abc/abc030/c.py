# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, M = map(int, raw_input().split())
X, Y = map(int, raw_input().split())
a = map(int, raw_input().split())
b = map(int, raw_input().split())

t, ans = 0, 0
i = j = 0
while 1:
    while i < N and a[i] < t:
        i += 1
    if i == N: break
    t = a[i] + X
    while j < M and b[j] < t:
        j += 1
    if j == M: break
    t = b[j] + Y
    ans += 1
print ans
