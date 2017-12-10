# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

p, a, b = map(int, raw_input().split())

if p >= b:
    print max(p - b, a) + b
else:
    print -1
