# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
k = 1
while (k + 1)*(k + 2)/2 < n: k += 1
print n - (k*(k + 1)/2)
