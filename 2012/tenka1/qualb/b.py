# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

s = raw_input()
for i in xrange(1, 10):
    if "_" + str(i) in s:
        print s
        exit()
t = s[0] 
snake = 0
for si in s[1:]:
    if t[-1] != "_" and t[-1].islower() and si.isupper():
        t += "_" + si.lower()
    elif snake and si != "_":
        t += si.upper()
        snake = 0
    elif t[-1] != "_" and si == "_":
        snake += 1
    else:
        t += si
t += "_" * snake
print t
