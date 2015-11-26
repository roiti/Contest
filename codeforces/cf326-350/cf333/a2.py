# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, b = map(int, raw_input().split())
x = map(int, raw_input().split())
X = 0
for xi in x:
    X = X * b + xi
n, b = map(int, raw_input().split())
y = map(int, raw_input().split())
Y = 0
for yi in y:
    Y = Y * b + yi

if X == Y:
    print "="
elif X < Y:
    print "<"
else:
    print ">"
