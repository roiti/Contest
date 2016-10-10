# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def is_kadomatsu(a, b, c):
    return a != b and b != c and c != a and (max((a, b, c)) == b or min((a, b, c)) == b)

A1, A2, A3 = map(int, raw_input().split())
ans = 0
for p in xrange(1, 1005):
    B1, B2, B3 = A1%p, A2%p, A3%p
    if is_kadomatsu(B1, B2, B3):
        ans += 1
print ans if not is_kadomatsu(A1, A2, A3) else "INF"
