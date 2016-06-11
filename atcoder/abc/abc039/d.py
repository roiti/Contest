#-*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def is_cand(x, y):
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < W and 0 <= ny < H): continue
        if S[ny][nx] != "#":
            return False
    return True

dxy = zip([1, 1, 0, -1, -1, -1, 0, 1], [0, 1, 1, 1, 0, -1, -1, -1])

H, W = map(int, raw_input().split())
S = [raw_input() for i in xrange(H)]

ans = [["."]*W for i in xrange(H)]
ok  = [[False]*W for i in xrange(H)]
for y in xrange(H):
    for x in xrange(W):
        if S[y][x] == "#" and is_cand(x, y):
            ans[y][x] = "#"
            ok[y][x] = True
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < W and 0 <= ny < H): continue
                ok[ny][nx] = True

for y in xrange(H):
    for x in xrange(W):
        if S[y][x] == "#" and not ok[y][x]:
            print "impossible"
            exit()

print "possible"
for line in ans:
    print "".join(line)
