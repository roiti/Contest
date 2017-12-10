# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def solve():
    N, A, B, C, D = map(int, raw_input().split()) 
    A, B = 0, B - A
    if B < 0: B *= -1
    M = N - 1

    for i in xrange(N):
        if C*(M - i) - D*i <= B <= D*(M - i) - C*i:
            return True

    return False

print "YES" if solve() else "NO"

