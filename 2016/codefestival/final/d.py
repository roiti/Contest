# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, M = map(int, raw_input().split())
X = map(int, raw_input().split())

cnt = [0]*100005
for x in X:
    cnt[x] += 1

pair = [0]*M
for i in xrange(100005):
    pair[i%M] += cnt[i]/2
    cnt[i] %= 2

mod = [0]*M
for i in xrange(100005):
    mod[i%M] += cnt[i]

ans = sum(pair)
for i in xrange(M):
    if i == 0 or i == M - i:
        ans += mod[i]/2 
        mod[i] %= 2
    else:
        m = min(mod[i], mod[M - i])
        ans += m
        mod[i] -= m
        mod[M - i] -= m

for i in xrange(1, M):
    while pair[i] >= 1 and mod[M - i] >= 2:
        ans += 1
        pair[i] -= 1
        mod[M - i] -= 2


print ans
