# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, m = map(int, raw_input().split())
a = [map(int, raw_input().split()) for i in xrange(n)]

g = [range(1, m + 1) for i in xrange(n)]
for i in xrange(m):
    for j in xrange(i, m):
        b = copy.deepcopy(a)
        for k in xrange(n):
            b[k][i] = a[k][j]
            b[k][j] = a[k][i]
        for k in xrange(n):
            cnt = 0
            for l in xrange(m):
                if b[k][l] != g[k][l]: cnt += 1
                if cnt > 2: break
            if cnt > 2: break
        else:
            print "YES"
            exit()
print "NO"
