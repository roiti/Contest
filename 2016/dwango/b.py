# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input()) 
K = map(int, raw_input().split())

A = sorted([(K[i], i) for i in xrange(N - 1)], reverse = True)
L = [1]*N

for Ki, i in A:
    L[i] = L[i + 1] = Ki

print " ".join(map(str, L))
