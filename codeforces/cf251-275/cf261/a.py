# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

x1, y1, x2, y2 = map(int, raw_input().split())
if x1 == x2:
    d = abs(y1 - y2)
    print x1 + d, y1, x2 + d, y2
elif y1 == y2:
    d = abs(x1 - x2)
    print x1, y1 + d, x2, y2 + d
elif abs(x1 - x2) == abs(y1 - y2):
    print x1, y2, x2, y1
else:
    print -1
