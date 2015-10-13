# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
a = map(int, raw_input().split())

ans = 0
s = sum(a)
if s % 3 == 0:
    x = s / 3
    y = 2 * x
    t = cnt = 0
    for ai in a[:-1]:
        t += ai
        if t == y:
            ans += cnt 
        if t == x:
            cnt += 1
print ans
