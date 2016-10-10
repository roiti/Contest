# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def gcd(a, b):
    while b: a, b = b, a%b
    return a

def extgcd(a, b):
    if b == 0: return [a, 1, 0]
    g, x, y = extgcd(b, a%b)
    return [g, y, x - a/b*y]

def crt(a0, m0, a1, m1):
    g = gcd(m0, m1)
    if a0%g != a1%g: return [-1, -1]
    if g > 1:
        m0 /= g
        m1 /= g
        while 1:
            gt = gcd(m0, g)
            if gt == 1: break
            m0 *= gt
            g /= gt
        m1 *= g
        a0 %= m0
        a1 %= m1
    g, p, q = extgcd(m0, m1)
    res = a0*q*m1 + a1*p*m0
    mod = m0*m1
    return [res%mod, mod]

def crts(a, m):
    res, mod = 0, 1
    for ai, mi in zip(a, m):
        ans, mod = crt(res, mod, ai, mi)
        if (res == -1): return [-1, -1]
    return [res, mod]

n, m, k = map(int, raw_input().split())
for loop in xrange(k):
    x, y = map(int, raw_input().split())
    ans = 1e10
    X = [x, x, 2*n - x, 2*n - x]
    Y = [y, 2*m - y, 2*m - y, y]
    for i in xrange(len(X)):
        t, mod = crt(X[i], 2*n, Y[i], 2*m)
        if t == -1:
            continue
        ans = min(ans, t)
    print ans if ans < 1e10 else -1 
