# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
H = sorted(map(int, raw_input().split()))
X = int(raw_input())
print bisect.bisect_left(H, X) + 1
