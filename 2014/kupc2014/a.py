# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

a1, a2, a3, b1, b2, b3 = map(int, raw_input().split())
ans = 10000
for c1, c2, c3 in it.permutations([a1, a2, a3], 3):
    ans = min(ans, abs(c1 - b1) + abs(c2 - b2) + abs(c3 - b3))
print ans
