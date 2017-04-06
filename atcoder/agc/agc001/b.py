# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, X = map(int, raw_input().split())


if X > N/2:
    alpha = X = N - X

ans = N
R = N - X
while R and X:
    if R%X == 0:
        ans += X + 2*(R/X - 1)*X
        break
    K = R/X
    ans += 2*K*X
    if R == 1: break
    R, X = X, R%X
print ans
