# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
K = int(raw_input())
X = int(raw_input())
Y = int(raw_input())
print X*min(K, N) + Y*max(0, N - K)
