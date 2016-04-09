# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

sys.setrecursionlimit(1000000)
mod = 10**9 + 7

def dfs(i):
    used[i] = True
    white, black = 1, 1
    for j in conn[i]:
        if used[j]: continue
        white_child, black_child = dfs(j)
        white = white * (white_child + black_child) % mod
        black = black * white_child % mod
    return white, black

N = int(raw_input())
used = [False] * N
conn = [[] for i in xrange(N)]
for i in xrange(N - 1):
    a, b = map(int, raw_input().split())
    conn[a - 1].append(b - 1)
    conn[b - 1].append(a - 1)

print sum(dfs(0)) % mod
