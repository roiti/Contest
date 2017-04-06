# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, M = map(int,raw_input().split())
A = [raw_input() for i in xrange(N)]
B = [raw_input() for i in xrange(M)]

for i in xrange(N - M + 1):
    for j in xrange(N - M + 1):
        same = True
        for y in xrange(M):
            for x in xrange(M):
                if A[i + y][j + x] != B[y][x]: same = False
            if not same: break
        if same:
            print "Yes"
            exit()
print "No"
