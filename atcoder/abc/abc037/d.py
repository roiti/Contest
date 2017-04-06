# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

mod = 10**9 + 7
dxy = zip([1, 0, -1, 0], [0, 1, 0, -1])

def is_inside(x, y):
    return 0 <= x < W and 0 <= y < H

H, W = map(int, raw_input().split())
a = [map(int, raw_input().split()) for i in xrange(H)]
comb = [[1]*W for i in xrange(H)]
order = sorted((a[i][j], i, j) for i in xrange(H) for j in xrange(W))

for _, y, x in order:
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if not is_inside(nx, ny): continue
        if a[ny][nx] > a[y][x]:
            comb[ny][nx] = (comb[ny][nx] + comb[y][x]) % mod

ans = 0
for i in xrange(H):
    for j in xrange(W):
        ans = (ans + comb[i][j]) % mod

print ans

