# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

T = int(raw_input())
for loop in xrange(T):
    S = raw_input()
    while len(S) > 1:
        U = ""
        for i, j in zip(S, S[1:]):
            x = int(i) + int(j)
            if x > 9: x = x/10 + x%10
            U += str(x)
        S = U
    print S
