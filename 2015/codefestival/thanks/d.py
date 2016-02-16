# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
s = [int(raw_input()) for i in xrange(N)]
S = sum(s)
s_know = s[:]
know = [[False]*N for i in xrange(N)]
n_know = [1]*N
for i in xrange(N):
    know[i][i] = True

M = int(raw_input())
for loop in xrange(M):
    a, b, c = map(int, raw_input().split())
    b -= 1
    c -= 1
    if a == 0:
        know[b][c] = True
        s_know[b] += s[c]
        n_know[b] += 1
    else:
        if know[b][c]:
            print s[c], s[c]
        else:
            rem = S - s_know[b]
            mn = max(0, rem - 100*(N - n_know[b] - 1))
            mx = min(100, rem)
            print mn, mx
