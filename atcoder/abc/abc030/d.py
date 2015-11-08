# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, a = map(int, raw_input().split())
k = int(raw_input())
b = map(int, raw_input().split())
used = [-1] * N

i = 0
while k:
    a = b[a - 1]
    k -= 1
    if used[a - 1] > -1:
        loop = i - used[a - 1]
        break
    used[a - 1] = i
    i += 1

if k > 0: k %= loop
for i in xrange(k):
    a = b[a - 1]

print a
