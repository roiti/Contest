# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def bitcount(n):
    return bin(n).count("1")

T = int(raw_input())
for loop in xrange(T):
    N = int(raw_input())
    X = N
    for i in xrange(66, -1, -1):
        if not (X >> i) & 1: continue
        NX = X ^ (1 << i)
        d = bitcount(NX) - bitcount(NX + N)
        if d < 0:
            for j in xrange(i - 1, -1, -1):
                if (X >> j) & 1: continue
                NNX = NX | (1 << j)
                dd = bitcount(NNX) - bitcount(NNX + N)
                if dd == 0:
                    X = NNX
                    break
        else:
            X = NX
    print X
