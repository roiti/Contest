# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
S = raw_input()

i = cnt = 0
while i < 2*N:
    if S[i:i+2] in ["10", "01"]:
        i += 2
    else:
        i += 1
    cnt += 1
print cnt - N
