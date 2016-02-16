# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def lcs(seq1, seq2):
    a, b = len(seq1), len(seq2)
    x1 = [0 for i in range(b+1)]
    for i in range(a):
        e1 = seq1[i]
        x2 = x1+[]
        for j in range(b):
            if e1 == seq2[j]:
                x1[j+1] = x2[j] + 1
            elif x1[j+1] < x1[j]:
                x1[j+1] = x1[j]
    return x1[-1]

N = int(raw_input())
S = raw_input()
ans = N
for i in xrange(N):
    ans = min(ans, N - 2*lcs(S[:i], S[i:]))
print ans
