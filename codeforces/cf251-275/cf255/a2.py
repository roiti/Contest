# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
c = raw_input()

i = 0 
while i < n and c[i] == "1": i += 1
print min(n, i + 1)
