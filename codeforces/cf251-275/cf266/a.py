# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, m, a, b = map(int, raw_input().split())
if m * a <= b:
    print n * a
else:
    d = n / m
    r = n % m
    print d * b + min(a * r, b)
