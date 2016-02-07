# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def gcd(a, b):
    while b: a, b = b, a%b
    return a

def lcm(a, b):
    return a/gcd(a, b)*b

N = int(raw_input())
a, b, c = map(int, raw_input().split())

print N/a + N/b + N/c - N/lcm(a,b) - N/lcm(b,c) - N/lcm(c,a) + N/lcm(lcm(a,b),c)
