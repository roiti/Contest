# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, K = map(int, raw_input().split())
boat = []
for i in xrange(K):
    boat.append(set(map(int, raw_input().split())[1:]))

ans = set() 
R = int(raw_input())
for i in xrange(R):
    p, q = map(int, raw_input().split()) 
    for k in xrange(K):
        if p in boat[k] and q in boat[k]:
            ans.add(p)
            ans.add(q)
print len(ans)
