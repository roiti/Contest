# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

T = int(raw_input())
for loop in xrange(T):
    s = raw_input()
    ans = i = 0
    while i + 5 <= len(s):
        if s[i:i + 5] == "kyoto":
            ans += 1
            i += 5
        elif s[i:i + 5] == "tokyo":
            ans += 1
            i += 5
        else:
            i += 1
    print ans
