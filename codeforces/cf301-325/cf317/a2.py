# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

na, nb = map(int, raw_input().split())
k, m = map(int, raw_input().split())
A = sorted(map(int, raw_input().split()))
B = sorted(map(int, raw_input().split()))

print "YES" if A[k - 1] < B[-m] else "NO"
