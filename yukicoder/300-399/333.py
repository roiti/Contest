# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

mx = 2*10**9
A, B = map(int, raw_input().split())
if A < B:
    print B - 2
else:
    print mx - 1 - B

