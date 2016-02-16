# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, m, k = map(int, raw_input().split())

if (n - 1) + (m - 1) < k:
    print -1
else:
    ans = max(m*(n/(k + 1)), n*(m/(k+1)))
    if n <= k + 1:
        ans = max(ans, m/(k - (n - 1) + 1))
    if m <= k + 1:
        ans = max(ans, n/(k - (m - 1) + 1))
    print ans
