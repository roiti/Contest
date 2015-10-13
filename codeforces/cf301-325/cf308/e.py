# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

s = "*" + raw_input() + "*"
n = len(s)
pos = []
for i in xrange(n):
    if s[i] == "*":
        pos.append(i)

m = len(pos)
ans = eval(s[1:-1]) 
for i in xrange(m):
    p = pos[i]
    for j in xrange(i + 1, m):
        q = pos[j]
        t = s[1:p + 1] + "(" + s[p + 1:q] + ")" + s[q:-1]
        ans = max(ans, eval(t))
print ans
