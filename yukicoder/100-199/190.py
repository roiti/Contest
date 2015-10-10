# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
A = map(int, raw_input().split())
A.sort()
B = A[::-1]

dry = wet = moist = 0
i = j = 0
while i + j < 2 * N - 1:
    if A[i] + B[j] < 0:
        i += 1
        dry += 1
    j += 1
i = j = 0
while i + j < 2 * N - 1:
    if A[i] + B[j] > 0:
        j += 1
        wet += 1
    i += 1
i = j = 0
while i + j < 2 * N - 1:
    if A[i] + B[j] == 0:
        i += 1
        j += 1
        moist += 1
    elif A[i] + B[j] < 0:
        i += 1
    else:
        j += 1
print dry, wet, moist
