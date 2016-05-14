# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
a = map(int, raw_input().split())

ans = 0
k = N
while a:
    x = a.pop()
    if x == k:
        k -= 1
    else:
        ans += 1
print ans
