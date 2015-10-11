# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, S = map(int, raw_input().split())
P = [int(raw_input()) for i in xrange(N)]

ans = []
dic = coll.defaultdict(list)
for i in xrange(1, N / 2 + 1):
    for s1 in it.combinations(range(N / 2), i):
        T = sum(P[j] for j in s1)
        if T == S: ans.append(s1)
        dic[T].append(s1)

for i in xrange(1, N - N / 2 + 1):
    for s2 in it.combinations(range(N / 2, N), i):
        T = sum(P[j] for j in s2)
        if T == S: ans.append(s2)
        if S - T in dic:
            for s1 in dic[S - T]:
                ans.append(s1 + s2)

ans = [[i + 1 for i in s] for s in ans]
ans.sort()
for s in ans:
    print " ".join(map(str, s))

