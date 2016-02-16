# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
a = map(int, raw_input().split())

cnt1 = coll.defaultdict(int)
cnt2 = coll.defaultdict(int)
for ai in a:
    cnt1[ai] += 1

ans = 0
for i in xrange(n - 1):
    cnt2[a[i]] += 1
    cnt1[a[i]] -= 1
    ans += min(cnt2[a[i]], cnt1[a[i + 1]])
print ans
