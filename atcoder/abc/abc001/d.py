# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
memo = []
for i in xrange(N):
    s, e = map(int, raw_input().split("-"))
    while s % 5 != 0: s -= 1
    while e % 5 != 0: e += 1
    if e % 100 == 60: e = e/100 * 100 + 100
    memo.append((s, e))
memo.sort()
ans = []
l, r = memo[0]
for s, e in memo[1:]:
    if l <= s <= r:
        r = max(r, e)
    else:
        ans.append((l, r))
        l, r = s, e
ans.append((l, r))
for l, r in ans:
    print "%04d-%04d" % (l, r)
