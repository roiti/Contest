# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

W, H = map(int, raw_input().split())
p = [int(raw_input()) for i in xrange(W)]
q = [int(raw_input()) for i in xrange(H)]
r = zip(p, [0]*W) + zip(q, [1]*H)
r.sort(reverse = True)
w, h = 0, 0
ans = sum(p)*(H + 1) + sum(q)*(W + 1) 
for x, k in r:
    if k == 0:
        ans -= max(0, (H - h)*x)
        w += 1
    else:
        ans -= max(0, (W - w)*x)
        h += 1
print ans
