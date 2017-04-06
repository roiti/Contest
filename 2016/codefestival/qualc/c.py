# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

mod = 10**9 + 7

N = int(raw_input())
T = map(int, raw_input().split())
A = map(int, raw_input().split())

hmin = [1]*N
hmax = [1]*N
hmin[0] = hmax[0] = T[0]
hmin[N - 1] = hmax[N - 1] = A[N - 1]

if T[N - 1] != A[0]:
    print 0
    exit()

for i in xrange(1, N - 1):
    if T[i] > T[i - 1]:
        hmin[i] = hmax[i] = T[i]
    else:
        hmax[i] = T[i]
for i in xrange(N - 2, 0, -1):
    if A[i] > A[i + 1]:
        if A[i] > hmax[i]:
            print 0
            exit()
        hmax[i] = hmin[i] = A[i]
    else:
        hmax[i] = min(hmax[i], A[i])

ans = 1
for i in xrange(N):
    ans = ans*(hmax[i] - hmin[i] + 1)%mod

print ans
