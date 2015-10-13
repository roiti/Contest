# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

alpha = "abcdefghijklmnopqrstuvwxyz"

s = raw_input()
ans = set()
for c in alpha:
    for i in xrange(len(s) + 1):
        ans.add(s[:i] + c + s[i:])
print len(ans)
