# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def solve():
    s = raw_input()
    N = len(s)
    for i in xrange(N - 1):
        if s[i] == s[i + 1]:
            return i + 1, i + 2
    for i in xrange(N - 2):
        if s[i] == s[i + 2]:
            return i + 1, i + 3
    return -1, -1

print " ".join(map(str, solve()))
