# -*- coding: utf-8 -*-
import sys,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def isprime(k):
    i = 2
    while i * i <= k:
        if k % i == 0: return False
        i += 1
    return True

n = int(raw_input())
ans = []
for i in xrange(2, n + 1):
    if isprime(i):
        ans.append(i)
        for j in xrange(2, 1000):
            if i ** j > n: break
            ans.append(i ** j)
print len(ans)
print " ".join(map(str, ans))
