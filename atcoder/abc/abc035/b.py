# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

S = raw_input()
T = int(raw_input())
x, y, q = 0, 0, 0
for s in S:
    if s == "L": x -= 1
    if s == "R": x += 1
    if s == "U": y += 1
    if s == "D": y -= 1
    if s == "?": q += 1

x, y = abs(x), abs(y)
if T == 1:
    print x + y + q
else:
    if x < q:
        q -= x
        x = 0
    else:
        x -= q
        q = 0

    if y < q:
        q -= y
        y = 0
    else:
        y -= q
        q = 0
    print x + y + q%2
