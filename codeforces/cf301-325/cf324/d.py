# -*- coding: utf-8 -*-
import sys,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def isprime(k):
    if k % 2 == 0: return False
    i = 3
    while i * i <= k:
        if k % i == 0: return False
        i += 2
    return True

n = int(raw_input())
if isprime(n):
    print 1
    print n
    exit()

m = n
m -= 2
if isprime(m):
    print 2
    print 2, m
    exit()

m = n
i = 1
m -= 3
a, b = 3, m - 3
while not (isprime(a) and isprime(b)):
    a += 2
    b -= 2
print 3
print 3, a, b
