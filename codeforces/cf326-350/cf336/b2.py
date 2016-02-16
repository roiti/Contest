# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

a = raw_input()
b = raw_input()

na, nb = len(a), len(b)
zero = one = 0

ans = 0
for i in xrange(nb - na):
    if b[i] == "0": zero += 1
    else: one += 1
for i in xrange(na):
    if b[i + nb - na] == "0": zero += 1
    else: one += 1

    if a[i] == "0":
        ans += one
    else:
        ans += zero

    if b[i] == "0": zero -= 1
    else: one -= 1

print ans
