# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

alpha = "abcdefghijklmnopqrstuvwxyz"

n = int(raw_input())
S = raw_input()
have = {c:0 for c in alpha}

ans = 0
for s in S:
    if s.islower():
        have[s] += 1
    else:
        if not have[s.lower()]:
            ans += 1
        else:
            have[s.lower()] -= 1
print ans
