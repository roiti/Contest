# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def pascal(n):
    line = [1]*(n + 1)
    for k in xrange(n):
        line[k + 1] = line[k]*(n - k)/(k + 1)
        if line[k + 1] > 9: line[k + 1] %= 9
    return line

P = dict()
T = int(raw_input())
for loop in xrange(T):
    S = raw_input()
    N = len(S)
    if N == 1:
        print S
        continue
    if N not in P:
        p = pascal(N - 1)
        P[N] = p
    else:
        p = P[N]
    X = 0
    for i, s in enumerate(S):
        X += int(s)*p[i]
    if X > 9: X %= 9
    print X 
