# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

inf = 1e9
dxy = zip([1, 0, -1, 0], [0, 1, 0, -1])

R, C = map(int, raw_input().split())
sy, sx = map(int, raw_input().split())
gy, gx = map(int, raw_input().split())
sy -= 1; sx -= 1; gy -= 1; gx -= 1
c = [raw_input() for i in xrange(R)]

dist = [[inf]*C for i in xrange(R)]
que = [[sx, sy]]
dist[sy][sx] = 0
while que:
    x, y = que.pop(0)

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if c[ny][nx] == "#": continue
        if dist[ny][nx] > dist[y][x] + 1:
            dist[ny][nx] = dist[y][x] + 1
            que.append([nx, ny])
            if (nx, ny) == (gx, gy):
                print dist[ny][nx]
                exit()
