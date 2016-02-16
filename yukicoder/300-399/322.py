# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
T = map(int, raw_input().split())
D = map(int, raw_input().split())

#s = sum(T)
s = sum(D) + N
ans = []
TD = zip(T, D, range(N))
while TD:
    #TD = sorted(sorted(TD, key = lambda x:x[1]), key = lambda x:(s - x[0])* (x[1] + 1))
    TD = sorted(sorted(TD, key = lambda x:x[1]), key = lambda x:x[0] * (s  - x[1]), reverse = True)
    t, d, i = TD.pop(0)
    ans.append(i + 1)
    s -= d + 1
#print " ".join(map(str, [(s - x[0])*(x[1] + 1) for x in TD]))
print " ".join(map(str, ans))
#print " ".join(map(str, [TD[i][2] + 1 for i in xrange(N)]))
