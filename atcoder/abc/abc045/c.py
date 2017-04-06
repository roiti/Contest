# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def calc(x, i):
    res = 0
    if i == N:
        j = 0
        for k in x:
            res += int(S[j:k])
            j = k
        return res
    for j in xrange(i + 1, N + 1):
        res += calc(x + [j], j)
    return res

S = raw_input()
N = len(S)
print calc([], 0)
