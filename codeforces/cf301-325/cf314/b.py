# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

a = [0] * 1000005
n = int(raw_input())
ans = use = 0
for loop in xrange(n):
    s, i = raw_input().split()
    i = int(i)
    if s == "+":
        a[i] = 1
        use += 1
    else:
        if a[i] == 1:
            a[i] = 0
            use -= 1
        else:
            ans += 1
    ans = max(ans, use)
print ans
