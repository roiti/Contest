# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def gcd(a, b):
    while b: a, b = b, a % b
    return a

N = int(raw_input())
A = [int(raw_input()) for i in xrange(N)]

g = A[0]
for a in A:
    g = gcd(a, g)

print sum(A)/g
