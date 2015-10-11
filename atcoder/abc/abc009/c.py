# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

alpha = "abcdefghijklmnopqrstuvwxyz"

def ok(i, k):
    CC = C.copy()
    for j in xrange(i, N):
        if CC[S[j]] > 0:
            CC[S[j]] -= 1
        else:
            k -= 1
    return k >= 0

N, K = map(int, raw_input().split())
S = raw_input()
C = {}
for c in alpha: C[c] = 0
for c in S:     C[c] += 1

ans = ""
for i in xrange(N):
    for c in alpha:
        if C[c] > 0:
            C[c] -= 1
            if S[i] != c:
                K -=1
            if ok(i + 1, K):
                ans += c
                break
            if S[i] != c:
                K += 1
            C[c] += 1

print ans
