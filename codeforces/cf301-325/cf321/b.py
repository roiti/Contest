# -*- coding: utf-8 -*-
import sys,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, d = map(int, raw_input().split())
ms = [map(int, raw_input().split()) for i in xrange(n)]
ms = sorted(ms)

ans = tmp = 0
i = j = 0
while j < n:
    if ms[j][0] - ms[i][0] < d:
        tmp += ms[j][1]
        j += 1
    else:
        tmp -= ms[i][1]
        i += 1
    ans = max(ans, tmp)
print max(ans, tmp)
