# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

dxy = zip([1, 0, -1, 0], [0, 1, 0, -1])

def slide(x, y):
    k = b[y][x]
    if k == 0: return -1, -1 
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 4 and a[ny][nx] == k:
            a[y][x], a[ny][nx] = a[ny][nx], a[y][x]
            return nx, ny
    return -1, -1 

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
b = [map(int, raw_input().split()) for i in xrange(4)]

x, y = 3, 3
while x != -1:
    x, y = slide(x, y)
print "Yes" if a == b else "No"
