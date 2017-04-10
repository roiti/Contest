# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll
 
K = int(raw_input())
 
cnt = 0
def rev_gcd(K):
    a, b = 1, 1
    for i in xrange(K):
        a, b = a + b, a
    return a, b
 
def gcd(a, b):
    global cnt
    while b:
        a, b = b, a % b
        cnt += 1
    return a
 
a, b = rev_gcd(K)
print a, b
gcd(a, b)
print cnt
