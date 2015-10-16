# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll


a, b, c = map(int, raw_input().split())
ans = []
for i in xrange(101):
    x = b * i ** a + c
    if 0 < x < 10 ** 9 and sum(map(int, str(x))) == i:
        ans.append(x)
print len(ans)
print " ".join(map(str, ans))
