# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
a = map(int, raw_input().split())
a = sorted([[ai, i] for i, ai in enumerate(a)], reverse = True, key = lambda x: x[0])
for ai, i in a:
    print i + 1
