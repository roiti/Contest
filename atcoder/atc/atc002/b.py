# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def mod_pow(a, p, mod):
    res = 1
    while p:
       if p & 1: res = res * a % mod
       a = a * a % mod
       p /= 2
    return res

N, M, P = map(int, raw_input().split())
print mod_pow(N, P, M)
#print pow(N, P, M)


