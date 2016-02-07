# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

ans = [20104, 20063, 19892, 20011, 19874, 20199, 19898, 20163, 19956, 19841]
s = raw_input().replace(".", "")
cnt = [0]*10
for si in s:
    cnt[int(si)] += 1

for i in xrange(10):
    if ans[i] < cnt[i]:
        a = i
    if ans[i] > cnt[i]:
        b = i
print a, b
