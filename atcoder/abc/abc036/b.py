# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
s = [raw_input() for i in xrange(N)]
for j in xrange(N):
    print "".join(s[i][j] for i in xrange(N - 1, -1, -1))

