# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

dxy = zip([1, 0, -1, 0], [0, 1, 0, -1])

def ok(x, y):
    B = copy.deepcopy(A)
    que = [[x, y]]
    while que:
        x, y = que.pop(0)
        if B[y][x] == "o":
            B[y][x] = "O"
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < 10 and 0 <= ny < 10): continue
                if B[ny][nx] != "o": continue
                que.append([nx, ny])
    for y in xrange(10):
        for x in xrange(10):
            if B[y][x] == "o":
                return False
    return True

A = [list(raw_input()) for i in xrange(10)]
for y in xrange(10):
    for x in xrange(10):
        if A[y][x] == "x":
            A[y][x] = "o"
            if ok(x, y):
                print "YES"
                exit()
            A[y][x] = "x"
print "NO"
