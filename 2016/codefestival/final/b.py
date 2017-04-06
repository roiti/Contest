# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())

s = 0
ans = []
for i in xrange(1, N + 1):
	ans.append(i)
	s += i
	if s >= N:
		k = s - N
		break

for i in ans:
	if i == k: continue
	print i
