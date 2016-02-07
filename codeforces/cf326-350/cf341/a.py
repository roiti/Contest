# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
a = map(int, raw_input().split()) 

s = sum(a)
if s % 2 == 0:
    print s
else:
    s -= min([ai for ai in a if ai % 2 == 1] + [10**10+1])
    print s
