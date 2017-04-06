# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

alpha = "abcdefghijklmnopqrstuvwxyz"
s = raw_input()
ans = 0
cur = "a"
for si in s:
    ans += min((alpha.index(cur) - alpha.index(si) + 26)%26, (alpha.index(si) - alpha.index(cur) + 26)%26)
    cur = si
print ans

