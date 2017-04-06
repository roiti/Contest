# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, K = map(int, raw_input().split())
P = set([raw_input() for i in xrange(N)])

cnt = [0]*26
for p in P:
    cnt[ord(p[0]) - ord("A")] += 1

ans = 0
while 1:
    cnt.sort(reverse = True)
    k = 0
    for i in xrange(26):
        if cnt[i] > 0:
            k += 1
            cnt[i] -= 1
        if k == K:
            ans += 1
            break
    else:
        break
print ans
