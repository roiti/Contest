# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

dxy = zip([1, 0, -1, 0], [0, 1, 0, -1])

def solve(x, y, n):
    if A[y][x] != "?" and A[y][x] != str(n): return False
    ans[y][x] = str(n)
    if n == 9:
        for line in ans:
            print "".join(line)
        return True

    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if not (0 <= nx < 3 and 0 <= ny < 3): continue
        if ans[ny][nx] != "": continue
        if solve(nx, ny, n + 1): return True
    ans[y][x] = ""

A = [raw_input() for i in xrange(3)]
ans = [[""]*3 for i in xrange(3)]
solve(1, 1, 1)

