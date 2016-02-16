# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

s = raw_input()
k = int(raw_input())
w = map(int, raw_input().split())
c = chr(w.index(max(w)) + ord("a"))
s += c * k

ans = 0
for i, si in enumerate(s):
    ans += w[ord(s[i]) - ord("a")] * (i + 1)
print ans
