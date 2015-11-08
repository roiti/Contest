# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, m = map(int, raw_input().split())
t = 30*(n%12) + 30*1.0/60*m - 6*m
if t < 0: t += 360
t = min(t, 360 - t)
print t
