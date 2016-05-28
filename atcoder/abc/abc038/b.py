# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

H1, W1 = map(int, raw_input().split())
H2, W2 = map(int, raw_input().split())

print "YES" if H1 == H2 or H1 == W2 or W1 == H2 or W1 == W2 else "NO"
