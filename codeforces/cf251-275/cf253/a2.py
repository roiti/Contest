# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

a = [0] * 26
s = raw_input()
for c in s:
    if c.isalpha():
        a[ord(c) - ord("a")] = 1
print sum(a)
