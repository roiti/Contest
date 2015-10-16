# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

cnt = [0] * 26
n, k = map(int, raw_input().split())
s = raw_input()
for si in s:
    cnt[ord(si) - ord("A")] += 1
cnt.sort(reverse = True)
ans = 0
for i in xrange(26):
    ans += min(k ** 2, cnt[i] ** 2)
    k -= min(k, cnt[i])
print ans
