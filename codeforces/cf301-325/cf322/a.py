# -*- coding: utf-8 -*-
import sys,math,heapq,itertools as it,fractions,re,bisect,collections as coll

a, b = map(int, raw_input().split())
mn, mx = min(a, b), max(a, b)
print mn, (mx - mn) / 2
