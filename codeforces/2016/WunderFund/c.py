# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def dist(x_y):
    x, y = x_y
    return x*x + y*y

n = int(raw_input())
xy = [map(int, raw_input().split()) for i in xrange(n)]
xy = [[xy[i], i] for i in xrange(n)]
xy = sorted(xy, key = lambda z: dist(z[0]))

i = 2
x0, y0 = xy[0][0]
x1, y1 = xy[1][0]
x2, y2 = xy[2][0]
while (x0*y1+x1*y2+x2*y0)-(x0*y2+x1*y0+x2*y1) == 0:
    i += 1
    x2, y2 = xy[i][0]
print " ".join(map(str, sorted([xy[0][1] + 1, xy[1][1] + 1, xy[i][1] + 1])))
