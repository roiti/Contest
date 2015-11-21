# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

A, B = map(int, raw_input().split())
x = (A + 1) * B
y = A * (B + 1)
print max(x, y)
