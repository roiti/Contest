# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

esp = 5e-13

p, q = map(int, raw_input().split())
p, q = p/100.0, q/100.0

ans = 1.0/3
que = coll.deque([[1.0/3, p]])
while que:
    ak, pk = que.popleft()
    ans += ak*pk*1.0/2
    ans += ak*(1 - pk)*1.0/3
    if ak*pk*1.0/2       > esp: que.append([ak*pk*1.0/2, max(0, pk - q)])
    if ak*(1 - pk)*1.0/3 > esp: que.append([ak*(1 - pk)*1.0/3, min(1, pk + q)])
print "%.10f" % ans
