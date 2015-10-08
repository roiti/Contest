# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

MX = 1180000 
prime = [1] * MX
prime[0] = prime[1] = 0
for i in xrange(2, int(MX ** 0.5 + 1e-8)):
    if prime[i]:
        prime[2 * i::i] = [0] * len(prime[2 * i::i])

p, q = map(int, raw_input().split())
pi = rub = ans = 0
for i in xrange(1, MX):
    pi += prime[i]
    if i == int(str(i)[::-1]): rub += 1
    if q * pi <= p * rub:
        ans = max(ans, i)

print ans
