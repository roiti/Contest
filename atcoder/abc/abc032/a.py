# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

a = int(raw_input())
b = int(raw_input())
n = int(raw_input())

def gcd(a, b):
    while b: a, b = b, a%b
    return a

x = a*b/gcd(a, b)

print int(math.ceil(1.0*n/x)*x)
