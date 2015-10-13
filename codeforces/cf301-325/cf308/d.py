# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def gcd(a, b):
    while b: a, b = b, a % b
    return a

n = int(raw_input())
xy = [map(int, raw_input().split()) for i in xrange(n)]

cnt = coll.defaultdict(int)
ans = n * (n - 1) * (n - 2) / 6
for i in xrange(n):
    xi, yi = xy[i]
    cnt.clear()
    for j in xrange(i + 1, n):
        xj, yj = xy[j]
        xj, yj = xj - xi, yj - yi
        g = gcd(abs(xj), abs(yj))
        xj, yj = xj / g, yj / g
        if xj < 0: xj, yj = -xj, -yj
        if yj == 0: xj, yj = 1, 0
        if xj == 0: xj, yj = 0, 1

        cnt[(xj, yj)] += 1
    for v in cnt.values():
        ans -= v * (v - 1) / 2 
print ans
