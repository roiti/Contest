# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, K = map(int, raw_input().split())
AB = [map(int, raw_input().split()) for i in xrange(N)]

b = bin(K)
bs = [K]
for i in xrange(len(b) - 1):
    nb = list(b)
    nb[i] = "0"
    nb[i + 1:] = ["1"]*len(nb[i + 1:])
    nb = int("".join(nb), 2)
    if nb <= K:
        bs.append(nb)

ans = 0
for v in bs:
    cur = 0
    for A, B in AB:
        if v|A <= v:
            cur += B
    ans = max(ans, cur)
print ans
