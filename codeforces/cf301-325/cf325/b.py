# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

t = int(raw_input())
for loop in xrange(t):
    n, k = map(int, raw_input().split())
    S = [raw_input() for i in xrange(3)]
    for y in xrange(3):
        if S[y][0] == "s":
            sx, sy = 0, y
            break
    que = [(sx, sy)]
    used = set()
    used.add((sx, sy))
    while que:
        x, y = que.pop()
        x = x + 1
        if x >= n:
            print "YES"
            break
        if S[y][x] != ".": continue
        for dy in xrange(-1, 2):
            ny = y + dy
            if not 0 <= ny <= 2: continue
            if S[ny][x] != ".": continue
            for dx in xrange(1, 3):
                nx = x + dx
                if nx >= n:
                    que.append((nx, ny))
                    continue
                if S[ny][nx] != ".":
                    break
            else:
                if (nx, ny) in used: continue
                que.append((nx, ny))
                used.add((nx, ny))
    else:
        print "NO"
