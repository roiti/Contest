# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

mod = 10**9 + 7;

N, K = map(int, raw_input().split())
a = map(int, raw_input().split())

def gcd(a, b):
    while (b): a, b = b, a%b
    return a

gcds = []
for i in xrange(N):
    g = a[i]
    for j in xrange(N):
        if i == j: continue
        g = min(g, gcd(a[i], a[j]))
        if g == 1: break
    gcds.append(g)

x = 1
for i in xrange(N):
    x *= a[i]

gcds = sorted(gcds, reverse = True)
print gcds
for i in xrange(max(1, N - 2*K)):
    x /= gcds[i];
print x
