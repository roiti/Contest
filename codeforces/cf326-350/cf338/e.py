# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())

lo,hi = 0, 10**18
while hi >= lo:
    mid = (hi + lo)/2
    if 6*mid*(mid + 1)/2 > n:
        hi = mid - 1
    else:
        lo = mid + 1

e = hi
m = n - 6*e*(e + 1)/2

x, y = 2*e, 0 
if m > 0:
    x += 1
    y += 2
    m -= 1

d = min(m, e)
x -= d
y += 2 * d
m -= d 

d = min(m, e + 1)
x -= 2 * d
m -= d

d = min(m, e + 1)
x -= d
y -= 2*d
m -= d

d = min(m, e + 1)
x += d
y -= 2*d
m -= d

d = min(m, e + 1)
x += 2*d
m -= d

d = min(m, e + 1)
x += d
y += 2*d
m -= d

print x, y
