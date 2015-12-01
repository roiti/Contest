# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

x = [500, 1000, 1500, 2000, 2500]
m = map(int, raw_input().split())
w = map(int, raw_input().split())
hs, hu = map(int, raw_input().split())

ans = sum(max(0.3*x[i], (1 - m[i]/250.0)*x[i] - 50*w[i]) for i in range(5))
ans += 100*hs - 50*hu
print int(ans)
