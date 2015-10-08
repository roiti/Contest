# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def judge(a, b, c):
    return a < b + c and b < a + c and c < a + b

a, b, c, l = map(int, raw_input().split())

ans = 0
for i in xrange(l + 1):
    A = a + i
    left = l - i
    ans += (left + 1) * (left + 2) / 2

for j in xrange(3):
    for i in xrange(l + 1):
        A = a + i
        left = l - i
        x = min(left, A - b - c)
        if x >= 0: ans -= (x + 1) * (x + 2) / 2

    if j == 0: a, b = b, a 
    if j == 1: a, c = c, a

print ans
