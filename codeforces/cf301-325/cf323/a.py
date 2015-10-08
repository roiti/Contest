# -*- coding: utf-8 -*-
import sys,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def gcd(a, b):
    while b: a, b = b, a % b
    return a

n = int(raw_input())
a = sorted(map(int, raw_input().split()))
cnt = coll.defaultdict(int)
ans = []
while a:
    e = a.pop()
    if cnt[e] > 0:
        cnt[e] -= 1
        continue
    for i in ans:
        g = gcd(i, e)
        cnt[g] += 2
    ans.append(e)
print " ".join(map(str, ans))
