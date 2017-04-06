# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

S = raw_input()
ans = 0

zero = False
for s in S:
    if s == "+":
        if not zero:
            ans += 1
        zero = False
    else:
        if s == "0":
            zero = True
if not zero:
    ans += 1
    
print ans
